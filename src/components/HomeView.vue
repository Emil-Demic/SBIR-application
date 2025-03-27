<script setup lang="ts">
import { pageState } from "../scope.ts";
import ImageDisplay from "./ImageDisplay.vue";
import SketchCanvas from "./SketchCanvas.vue";
</script>

<template>
    <SketchCanvas  />
    <hr>
    <div v-if="pageState.loading">
        <div class="d-flex justify-content-center mb-3">
            <div class="spinner-border" role="status">
                <span class="visually-hidden"></span>
            </div>
        </div>
    </div>
    <div v-else>
        <ImageDisplay  />
    </div>
</template>