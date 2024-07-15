from pathlib import Path
import openai

import os
import time
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

filename = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))

speech_dir_path = Path("/mnt/c/Users/hands/PycharmProjects/CR-bot/speech")
speech_file_path = speech_dir_path / f"{filename}.mp3"

# 디렉토리 생성 (존재하지 않을 경우)
speech_dir_path.mkdir(parents=True, exist_ok=True)

response = openai.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="The quick brown fox jumped over the lazy dog."
)
response.stream_to_file(speech_file_path)
# response.with_streaming_response().stream_to_file(str(speech_file_path))

# 음성 파일 재생
os.system(f"mpg321 {speech_file_path}")