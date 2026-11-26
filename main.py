import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui
import subprocess
import datetime
import os

# Mesh AI Assistant
engine = pyttsx3.init()
engine.setProperty("rate", 175)

recognizer = sr.Recognizer()


# اسسٹنٹ کی آواز
def speak(text):
    print("MESH:", text)
    engine.say(text)
    engine.runAndWait()


# آپ کی آواز سننا
def listen():
    try:
        with sr.Microphone() as source:

            print("Listening...")

            recognizer.adjust_for_ambient_noise(
                source, duration=0.5
            )

            audio = recognizer.listen(
                source, timeout=5, phrase_time_limit=7
            )

            command = recognizer.recognize_google(
                audio, language="en-US"
            ).lower()

            print("You:", command)

            return command

    except Exception:
        return ""


# ایپس کھولنا
def open_app(app):

    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "chrome": "chrome.exe",
        "file explorer": "explorer.exe"
    }

    if app in apps:
        try:
            subprocess.Popen(apps[app])
            speak(app + " کھول رہا ہوں")

        except Exception:
            speak("ایپ نہیں کھل سکی")


# کمانڈز
def execute_command(command):

    if "open chrome" in command:
        open_app("chrome")

    elif "open notepad" in command:
        open_app("notepad")

    elif "open calculator" in command:
        open_app("calculator")

    elif "open paint" in command:
        open_app("paint")

    elif "open file explorer" in command:
        open_app("file explorer")

    # Instagram
    elif "open instagram reels" in command:
        webbrowser.open(
            "https://www.instagram.com/reels/"
        )
        speak("انسٹاگرام ریلز کھول رہا ہوں")

    elif "open instagram" in command:
        webbrowser.open(
            "https://www.instagram.com/"
        )
        speak("انسٹاگرام کھول رہا ہوں")

    # Facebook
    elif "open facebook" in command:
        webbrowser.open(
            "https://www.facebook.com/"
        )
        speak("فیس بک کھول رہا ہوں")

    # YouTube
    elif "open youtube" in command:
        webbrowser.open(
            "https://www.youtube.com/"
        )
        speak("یوٹیوب کھول رہا ہوں")

    # Google
    elif "open google" in command:
        webbrowser.open(
            "https://www.google.com/"
        )
        speak("گوگل کھول رہا ہوں")

    # Volume Control
    elif "volume up" in command:
        pyautogui.press("volumeup", presses=5)
        speak("آواز بڑھا دی ہے")

    elif "volume down" in command:
        pyautogui.press("volumedown", presses=5)
        speak("آواز کم کر دی ہے")

    elif "mute" in command:
        pyautogui.press("volumemute")
        speak("آواز بند کر دی ہے")

    # Scroll
    elif "scroll down" in command:
        pyautogui.scroll(-5)
        speak("نیچے اسکرول کر رہا ہوں")

    elif "scroll up" in command:
        pyautogui.scroll(5)
        speak("اوپر اسکرول کر رہا ہوں")

    # Time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime(
            "%I:%M %p"
        )
        speak("وقت ہے " + current_time)

    # Date
    elif "date" in command:
        today = datetime.datetime.now().strftime(
            "%d %B %Y"
        )
        speak("آج کی تاریخ " + today)

    # Browser بند کرنا
    elif "close browser" in command:
        speak("براؤزر بند کر رہا ہوں")
        os.system("taskkill /im chrome.exe /f")

    # Assistant بند کرنا
    elif "exit assistant" in command or "stop assistant" in command:
        speak("خدا حافظ، Mesh Assistant بند ہو رہا ہے")
        return False

    else:
        speak("معذرت، میں آپ کی کمانڈ نہیں سمجھ سکا")

    return True


# اسسٹنٹ شروع کرنا
def start_assistant():

    speak("السلام علیکم! میں Mesh AI Assistant ہوں")

    speak("میں آپ کے حکم کا انتظار کر رہا ہوں")

    running = True

    while running:

        command = listen()

        if command:
            running = execute_command(command)


if __name__ == "__main__":
    start_assistant()
