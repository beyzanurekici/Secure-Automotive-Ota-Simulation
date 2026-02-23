from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

FIRMWARE_PATH = "server/firmware_v2.bin"
SIGNATURE_PATH = "server/firmware_v2.sig"

@app.get("/version")
def get_version():
    return {"version": "1.5.0"}

@app.get("/firmware")
def get_firmware():
    if os.path.exists(FIRMWARE_PATH):
        return FileResponse(FIRMWARE_PATH, media_type="application/octet-stream")
    return {"error": "Firmware not found"}

@app.get("/signature")
def get_signature():
    if os.path.exists(SIGNATURE_PATH):
        return FileResponse(SIGNATURE_PATH, media_type="application/octet-stream")
    return {"error": "Signature not found"}