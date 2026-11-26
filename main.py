import os
import webbrowser
import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.utils import platform

from jnius import autoclass


class MeshAIApp(App):

    def build(self):

        self.title = "Mesh AI Assistant"

        layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=20
        )

        self.status = Label(
            text="MESH AI ASSISTANT",
            font_size=28,
            color=(0, 0.8, 1, 1)
        )

        layout.add_widget(self.status)

        self.info = Label(
            text="Your Personal Voice Assistant",
            font_size=18
        )

        layout.add_widget(self.info)

        self.mic_button = Button(
            text="🎤 START LISTENING",
            font_size=22,
            size_hint=(1, 0.3),
            background_color=(0, 0.5, 1, 1)
        )

        self.mic_button.bind(
            on_press=self.listen_voice
        )

        layout.add_widget(self.mic_button)

        self.command_label = Label(
            text="Waiting for your command..."
        )

        layout.add_widget(self.command_label)

        return layout

    def speak(self, text):

        self.status.text = text

        if platform == "android":
            PythonActivity = autoclass(
                'org.kivy.android.PythonActivity'
            )

            activity = PythonActivity.mActivity

            Context = autoclass(
                'android.content.Context'
            )

            tts = activity.getSystemService(
                Context.TEXT_TO_SPEECH
            )

            if tts:
                Locale = autoclass('java.util.Locale')
                tts.setLanguage(Locale.US)
                tts.speak(
                    text,
                    0,
                    None,
                    "mesh_message"
                )

    def listen_voice(self):

        self.status.text = "Listening..."

        self.command_label.text = (
            "Speak your command..."
        )

        if platform == "android":

            try:
                PythonActivity = autoclass(
                    'org.kivy.android.PythonActivity'
                )

                Intent = autoclass(
                    'android.content.Intent'
                )

                RecognizerIntent = autoclass(
                    'android.speech.RecognizerIntent'
                )

                intent = Intent(
                    RecognizerIntent.ACTION_RECOGNIZE_SPEECH
                )

                intent.putExtra(
                    RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                    RecognizerIntent.LANGUAGE_MODEL_FREE_FORM
                )

                intent.putExtra(
                    RecognizerIntent.EXTRA_LANGUAGE,
                    "en-US"
                )

                activity = PythonActivity.mActivity

                activity.startActivityForResult(
                    intent, 1001
                )

                self.status.text = "Voice recognition opened"

            except Exception as e:
                self.status.text = str(e)

        else:
            self.status.text = "Android device required"

    def execute_command(self, command):

        command = command.lower()

        self.command_label.text = command

        if "instagram reels" in command:

            webbrowser.open(
                "https://www.instagram.com/reels/"
            )

            self.speak("Opening Instagram Reels")

        elif "instagram" in command:

            webbrowser.open(
                "https://www.instagram.com/"
            )

            self.speak("Opening Instagram")

        elif "facebook" in command:

            webbrowser.open(
                "https://www.facebook.com/"
            )

            self.speak("Opening Facebook")

        elif "youtube" in command:

            webbrowser.open(
                "https://www.youtube.com/"
            )

            self.speak("Opening YouTube")

        elif "google" in command:

            webbrowser.open(
                "https://www.google.com/"
            )

            self.speak("Opening Google")

        elif "time" in command:

            now = datetime.datetime.now().strftime(
                "%I:%M %p"
            )

            self.speak("The time is " + now)

        elif "date" in command:

            today = datetime.datetime.now().strftime(
                "%d %B %Y"
            )

            self.speak("Today's date is " + today)

        elif "scroll down" in command:

            self.speak("Scroll down command received")

        elif "scroll up" in command:

            self.speak("Scroll up command received")

        else:

            self.speak("Command not recognized")


if __name__ == "__main__":
    MeshAIApp().run()
