import discord
from fastapi import FastAPI
from pydantic import BaseModel
from app.main import *

app = FastAPI()

@app.get("/")
def read_main():
    return "Le Seigneur des anneaux"

class TestClient:
    def __init__(self, app):
        self.app = app

    async def send_message(self, message):
        channel = await self.app.fetch_channel(123456789)
        await channel.send(message)
