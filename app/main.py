import utils.http_session
import utils.transport
import utils.session
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

