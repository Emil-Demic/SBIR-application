<template>
<div class="d-flex justify-content-center">
    <div class="mt-3">
        <h5>Sketch the image you would like to search for:</h5>
        <canvas ref="fabricCanvas" height="448" width="448" class="border border-black border-2" ></canvas>
        <div class="d-flex justify-content-between mt-2">
            <div>
                <n-button class="m-1" @click="undo">UNDO</n-button>
                <n-button class="m-1" @click="clearCanvas">CLEAR</n-button>
            </div>
            <n-button class="m-1" type="primary" @click="uploadCanvas">SEARCH</n-button>
        </div>
    </div>
</div>
</template>

<script setup lang="ts">
import { onMounted, useTemplateRef } from "vue";
import { indicies, pageOpt, pageState } from "../scope.ts";
import { NButton } from "naive-ui";
import * as fabric from "fabric";
import ky from 'ky';

const fabricCanvas = useTemplateRef("fabricCanvas");
let canvas : fabric.Canvas;
const state : string[] = [];
let currentStateIndex = -1;

onMounted(() => {
    canvas = new fabric.Canvas(fabricCanvas.value!, {
        isDrawingMode: true,
    });

    if (window.innerWidth < 500) {
        canvas.setDimensions({
            width: window.innerWidth * 0.9,
            height: window.innerWidth * 0.9    
        });
        pageOpt.perPage = 10;
    }

    canvas.freeDrawingBrush = new fabric.PencilBrush(canvas);
    canvas.freeDrawingBrush.color = "#000";
    canvas.freeDrawingBrush.width = 3;

    saveState();
    canvas.on('mouse:up', saveState);

    canvas.backgroundColor = "white";
});

const saveState = () => {
    if (currentStateIndex < state.length - 1) {
        state.splice(currentStateIndex + 1, state.length - currentStateIndex - 1);
    }
    state.push(JSON.stringify(canvas.toJSON()));
    currentStateIndex = state.length - 1;
}

const undo = () => {
    if (currentStateIndex > 0) {
        currentStateIndex--;
        canvas.loadFromJSON(state[currentStateIndex], function () {
            canvas.requestRenderAll();
        });
    }
}

const clearCanvas = () => {
    canvas.clear();
    canvas.backgroundColor = "white";
};

const uploadCanvas = async () => {
    // @ts-expect-error String is expected, TS refers to old documentation as far as I can tell
    const imageBase64 = canvas.toDataURL("image/png");
    pageState.loading = true;
    try{
        indicies.arr = await ky.post('https://sygvg7y3xr4kz36dtae5r72lx40tadxp.lambda-url.eu-central-1.on.aws/', {json: { image: imageBase64 }}).json();
        pageOpt.currIdx = 1;
    } catch (error) {
        console.error("Error fetching data:", error);
    } finally {
        pageState.loading = false;
    }
};
</script>