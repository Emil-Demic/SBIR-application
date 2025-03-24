<script setup>
import SketchCanvas from './components/SketchCanvas.vue';
import ImageDisplay from './components/ImageDisplay.vue';
import About from './components/About.vue';
import { pageState } from "./scope.js";
import { NButton } from "naive-ui";

const openGithub = () => {
    window.location.href = 'https://github.com/Emil-Demic/SBIR-frontend';
};
</script>

<template>
<div>
    <nav class="navbar navbar-expand bg-body-secondary">
        <div class="container-fluid">
            <n-button text class="navbar-brand" @click="pageState.about = false">SBIR ConvNeXt-InfoNCE</n-button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav ms-auto" >
                    <n-button text class="nav-link" @click="pageState.about = true">About</n-button>
                    <n-button text class="nav-link" @click="openGithub" >Github</n-button>
                </div>
            </div>
        </div>
    </nav>
    <div v-if="pageState.about">
        <About></About>
    </div>
    <div v-else>
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
    </div>
</div>
</template>
