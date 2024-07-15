import io

from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

import json

filename = ""

def transcribe_file_v2(project_id, recognizer_id, audio_file):
    client = SpeechClient()

    request = cloud_speech.CreateRecognizerRequest(
        parent=f"projects/{project_id}/loca",
        recognizer_id=recognizer_id,
        recogizer=cloud_speech.Recognizer(
            language_codes=["kor"],
            model="latest_long"
        )
    )

    operation = client.create_recognizer(request=request)
    recognizer = operation.result()

    with io.open(audio_file, "rb") as f:
        content = f.read()

        config = cloud_speech.RecognitionConfig(auto_decoding_config={})

        request = cloud_speech.RecognizeRequest(
            recognizer=recognizer.name, config=config, content=content
        )

        # Transcribes the audio into text
        response = client.recognize(request=request)
        data = []
        for result in response.results:
            data.append(result.alternatives[0].transcript)

        with open(filename, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        f.close()
        return response