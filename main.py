import requests
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from httpx import AsyncClient
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

KAKAO_CLIENT_ID = os.environ['KAKAO_CLIENT_ID']
KAKAO_CLIENT_SECRET = os.environ['KAKAO_CLIENT_SECRET']
KAKAO_REDIRECT_URI = os.environ['KAKAO_REDIRECT_URI']

# app.mount("/static", StaticFiles(directory="static"), name="static")
print(KAKAO_CLIENT_SECRET)


# @app.get("/")
# async def read_root():
#     return {"message": "Welcome to Kakao OAuth with FastAPI"}


@app.get("/")
async def kakao_login():
    kakao_auth_url = (
        f"https://kauth.kakao.com/oauth/authorize?response_type=code&scope=friends"
        f"&client_id={KAKAO_CLIENT_ID}&redirect_uri={KAKAO_REDIRECT_URI}"
    )
    return RedirectResponse(url=kakao_auth_url)


@app.get("/auth/kakao/callback")
async def kakao_callback(code: str):
    async with AsyncClient() as client:
        token_url = "https://kauth.kakao.com/oauth/token"
        token_data = {
            "grant_type": "authorization_code",
            "client_id": KAKAO_CLIENT_ID,
            "redirect_uri": KAKAO_REDIRECT_URI,
            "code": code,
            "client_secret": KAKAO_CLIENT_SECRET
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        token_response = await client.post(token_url, data=token_data, headers=headers)

        if token_response.status_code != 200:
            raise HTTPException(status_code=token_response.status_code, detail="Failed to fetch token")

        token_json = token_response.json()
        access_token = token_json.get("access_token")
        if access_token:
            response = requests.get("https://kapi.kakao.com/v1/api/talk/friends",
                                    headers={'Authorization': f"Bearer {access_token}"})
            if response.status_code == 200:
                return JSONResponse(content=response.json())
            else:
                raise HTTPException(status_code=response.status_code, detail=response.text)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
