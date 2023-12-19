import os
import logging
from fastapi import FastAPI

from src.routes.route import router

app = FastAPI(description='User authentication with the help of JWT.', title='UserAuth-Docker', version='1.1.1')
logging.basicConfig(level=logging.DEBUG)

# print env vars
logging.info("env vars: " + str(os.environ))

# Add route for APIs
app.include_router(router)


@app.get("/")
async def index():
    return "User Auth Service is running."
