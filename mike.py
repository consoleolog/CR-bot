import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Use the correct device index obtained from the previous step
device_index = 0  # Replace with the correct index from the PyAudio script

def stt():
    try:
        # Use the specified microphone
        mic = sr.Microphone(device_index=device_index)
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Say something!")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        try:
            result = r.recognize_google(audio, language="ko-KR")
            print(result)
            return result
        except sr.UnknownValueError:
            print("음성 인식 실패")
        except sr.RequestError:
            print("HTTP Request Error 발생")
        except sr.WaitTimeoutError:
            print("WaitTimeout Error 발생 ㅠㅠ")
    except AssertionError as e:
        print(f"Error: {e}")
