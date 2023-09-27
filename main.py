from fastapi import FastAPI
from wakeonlan import send_magic_packet

app = FastAPI()


@app.get("/")
def read_root():
    send_magic_packet("58.11.22.AE.7E.38")
    return {"message": "It's working!"}
