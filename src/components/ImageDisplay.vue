<template>
<div class="container">
    <div class="row row-cols-2 row-cols-lg-4">
        <template v-for="img in paginatedImages" :key="img">
            <div class="col gx-2 gy-3" style="aspect-ratio: 1;">
                <n-image :src="img" object-fit="contain" width="100%" />
            </div>
        </template>
    </div>
</div>
<div class="d-flex justify-content-center mt-2 mb-4">
    <n-pagination v-model:page="pageOpt.currIdx" :page-count="totalPages" simple size="large" />
</div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { NImage, NPagination } from 'naive-ui';
import { indicies, pageOpt } from "../scope.ts";

const CDN_URL = "https://d2f5e6rx1vgqv1.cloudfront.net/CDN_images/"

const img_links = computed(() => {
    return indicies.arr.map(id => `${CDN_URL}${id}.jpg`);
})

const totalPages = computed(() => Math.ceil(img_links.value.length / pageOpt.perPage));

const paginatedImages = computed(() => {
    const start = (pageOpt.currIdx - 1) * pageOpt.perPage;
    return img_links.value.slice(start, start + pageOpt.perPage);
});
</script>
