from pathlib import Path
import openai

import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# create speech
speech_file_path = Path(__file__).parent # speech.mp3
response = openai.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="The quick brown fox jumped over the lazy dog."
)
response.stream_to_file(speech_file_path)

# create transcription
from openai import OpenAI
client = OpenAI()

audio_file = open("speech.mp3","rb")
transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)
