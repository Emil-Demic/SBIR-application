<template>
    <div class="container">
        <div class="row my-3">
            <div class="col"></div>
            <div class="col-8">
                <h3>The App</h3>
                <p>This application showcases the practical implementation of a novel scene-level sketch-based image retrieval model, developed as the capstone project for my bachelor's degree.            </p>
                <p>To use the app, browse through the displayed images and select one. Then, sketch the image and press "Search." The app will sort the images from most to least similar to your sketch based on the model's predictions.</p>
                <p>The backend is deployed on an AWS Lambda function, so there may be a slight delay in search results, particularly for the first query.</p>
                <h3>The Model</h3>
                <p>The model is designed as a simple Siamese neural network, utilizing the ConvNeXt-Small CNN architecture as its encoder. The encoder was pre-trained on ImageNet, and the final model was fine-tuned for SBIR on the FSCOCO dataset using the InfoNCE loss function.</p>
                <img src="../assets/siameseNetFinal.png" width="80%" class="mx-auto d-block">
                <p>More information about the model is available on <a href="https://github.com/Emil-Demic/ConvNext-InfoNCE-SBIR">GitHub</a>, with additional details on its design and evaluation provided in the <a href="https://repozitorij.uni-lj.si/IzpisGradiva.php?id=167773&lang=eng">thesis (available only in Slovene)</a>.</p>
                <p>Despite its simplicity, the model significantly outperforms other baseline models on the FSCOCO dataset.</p>
                <h3>The Gallery</h3>
                <p>The images in the app come from the FSCOCO test set, using the "unseen users" train/test split. This set contains 3,000 images, representing a diverse range of complex real-world scenes.</p>
                <p>The model was trained on a dataset of 7,000 sketch-image pairs.</p>
            </div>
            <div class="col"></div>
        </div>
    </div>
</template>