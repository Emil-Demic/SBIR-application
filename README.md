# SBIR-frontend

[Available online](https://app.sbir.emil-demic.xyz/)

This application showcases the practical implementation of a novel scene-level sketch-based image retrieval model. \
To use the app, browse through the displayed images and select one. Then, sketch the image and press "Search." The app will sort the images from most to least similar to your sketch based on the model's predictions.
The Gallery \
The model is available in its own [repository](https://github.com/Emil-Demic/ConvNext-InfoNCE-SBIR) (will be made public upon paper acceptance).

## The Frontend

The application is built with Vue and utilizes the NaiveUI component library along with Bootstrap. It is hosted on AWS Amplify, while the images are served through AWS CloudFront CDN.

## The backend

The repository's *Backend* directory contains multiple possible backend solutions, each organized in its own subdirectory with a corresponding README. The recommended option for deployment is LitServe, which is also the one currently used for the online deployment.

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```
