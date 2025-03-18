import os
import redis.asyncio as redis
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN_FOR_BOT")
CHAT_ID = -4712679822
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)