### Example Code for Serving a Model in a Django App Using Django REST Framework and PostgreSQL with the pgvector Extension
The app uses *uv* for Python dependency management. If you don't have *uv* installed, install it first. From the app directory, run:

```sh
uv run <program>
```
*uv* will automatically install the required dependencies and run the program.

Alternatively, you can use another dependency management tool to install the dependencies listed in the *pyproject.toml* file.

Set up you PostgreSQL database and make sure pgvector is supported.
Applying already present migrations will enable the pgvector extension.

Place the pretrained model and the precomputed embeddings of galley images in the *api* folder.

Refer to Django documentation for detailed deployment instructions.