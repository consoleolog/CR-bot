import pyttsx3


def speak_text(text, rate=150, volume=1.0, voice_id=None):
    engine = pyttsx3.init()
    # 속도 설정
    engine.setProperty('rate', rate)
    # 볼륨 설정
    engine.setProperty('volume', volume)
    # 목소리 유형 설정
    if voice_id:
        engine.setProperty('voice', voice_id)

    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    print("Available voices:")
    for idx, voice in enumerate(voices):
        print(f"{idx}: {voice.name} ({voice.id})")

    while True:
        text = input("Enter text to speak (or 'exit' to quit): ")
        if text.lower() == 'exit':
            break
        rate = 150
        volume = 1
        voice_choice = 17
        voice_id = voices[voice_choice].id

        speak_text(text, rate, volume, voice_id)
