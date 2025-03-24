# SBIR-frontend

This application showcases the practical implementation of a novel scene-level sketch-based image retrieval model, developed as the capstone project for my bachelor's degree. \
To use the app, browse through the displayed images and select one. Then, sketch the image and press "Search." The app will sort the images from most to least similar to your sketch based on the model's predictions. \
The model is available in its own [repository](https://github.com/Emil-Demic/ConvNext-InfoNCE-SBIR).

## The Frontend

The application is built with Vue and utilizes the NaiveUI component library along with Bootstrap. It is hosted on AWS Amplify, while the images are served through AWS CloudFront CDN.

## The backend

The backend is written in Python and runs on an AWS Lambda function. The backend code can be found in the *Backend* directory.

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
