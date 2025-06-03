<template>
    <div class="container">
        <div class="row my-3">
            <div class="col"></div>
            <div class="col-8">
                <h3>The App</h3>
                <p>This application showcases the practical implementation of a novel scene-level sketch-based image retrieval model.</p>
                <p>To use the app, browse through the displayed images and select one. Then, sketch the image and press "Search." The app will sort the images from most to least similar to your sketch based on the model's predictions.</p>
                <h3>The Gallery</h3>
                <p>The images in the app come from the FSCOCO test set, using the "unseen users" train/test split. This set contains 3,000 images, representing a diverse range of complex real-world scenes.</p>
                <p>The model was trained on a dataset of 7,000 sketch-image pairs.</p>
                <h3>The Model</h3>
                <p>The model follows a straightforward Siamese neural network architecture, employing a pretrained ConvNeXt convolutional backbone as its encoder. This encoder was fine-tuned for sketch-based image retrieval on the FSCOCO dataset using a contrastive loss function.</p>
                <img src="../assets/model-1.png " width="80%" class="mx-auto d-block">
                <p>Additional information about the model is available on <a href="https://github.com/Emil-Demic/ConvNext-InfoNCE-SBIR">GitHub</a> (the code will be released upon paper acceptance).Further details on its design and evaluation can be found in <a href="https://repozitorij.uni-lj.si/IzpisGradiva.php?id=167773&lang=eng">the thesis</a>, which is only available in Slovene.</p>
                <p>Despite its simplicity, the model significantly outperforms other baseline models on the FSCOCO dataset.</p>
                
            </div>
            <div class="col"></div>
        </div>
    </div>
</template>