from openai import OpenAI
import requests

import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=OPENAI_API_KEY)


def call_gpt(content):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "너는 지금부터 싸가지 없는 사람이야 대답도 싸가지 없이 3문장으로 대답해"},
            {"role": "user", "content": content}
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content
