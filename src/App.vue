<script setup>
import { NButton } from "naive-ui";

const openGithub = () => {
    window.location.href = 'https://github.com/Emil-Demic/SBIR-frontend';
};
</script>

<template>
<div>
    <nav class="navbar navbar-expand bg-body-secondary">
        <div class="container-fluid">
            <n-button text class="navbar-brand" @click="$router.push('/')">SBIR ConvNeXt-InfoNCE</n-button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav ms-auto" >
                    <n-button text class="nav-link" @click="$router.push('/about')">About</n-button>
                    <n-button text class="nav-link" @click="openGithub" >Github</n-button>
                </div>
            </div>
        </div>
    </nav>
    <main>
        <RouterView />
    </main>
</div>
</template>
