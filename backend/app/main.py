from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Chatkie API", version="1.0.0")
origins = [x.strip() for x in os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",") if x.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
async def root():
    return {"name": "Chatkie API", "status": "running", "note": "Existing authentication, realtime database and WebRTC signaling remain on the configured Firebase/P2P path until their staged migration."}

@app.get("/health")
async def health():
    return {"ok": True}

@app.websocket("/ws/health")
async def websocket_health(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            message = await ws.receive_text()
            await ws.send_json({"type": "ack", "message": message})
    except WebSocketDisconnect:
        pass
