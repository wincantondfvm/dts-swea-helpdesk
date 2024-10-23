from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

OPENAPI_URL = "/api/py/openapi.json"
app = FastAPI(openapi_url=OPENAPI_URL)


@app.get("/api/py/docs")
def docs():
    return get_scalar_api_reference(openapi_url=OPENAPI_URL, title="Docs")


@app.get("/api/py/hello")
def hello():
    return {"message": "Hello, world!"}
