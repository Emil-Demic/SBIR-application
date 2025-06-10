### Example code for running a model server using LitServe (Preferred option)
The app uses *uv* for Python dependency management. If you don't have *uv* installed, install it first. From the app directory, run:

```sh
uv run main.py
```
*uv* will automatically install the required dependencies and run the program.

Alternatively, you can use another dependency management tool to install the dependencies listed in the *pyproject.toml* file.

Make sure to place the pretrained model and the precomputed embeddings of gallery images in the folder with the app.

To expose the server, configure your preferred reverse proxy (e.g., nginx) to route traffic appropriately.