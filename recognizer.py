import speech_recognition as sr
import os

def speech_to_text(file_name):

    r = sr.Recognizer()
    try:
        with sr.AudioFile(file_name) as source:
            audio_data = r.record(source)
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return None
    try:
        text = r.recognize_sphinx(audio_data)
        return text
    except sr.RequestError:
        print("Could not request results from Sphinx service.")
        return None
    except sr.UnknownValueError:
        print("Sphinx could not understand audio.")
        return None

def save_text_to_file(text, file_name):
    if text is not None:
        with open(file_name, 'w') as file:
            file.write(text)

def main():
    file_name = 'two.wav'
    text = speech_to_text(file_name)
    print(text)

    if text is not None:
        output_file = 'output.txt'
        save_text_to_file(text, output_file)
        print(f"Text saved to {output_file}")

if __name__ == "__main__":
    main()