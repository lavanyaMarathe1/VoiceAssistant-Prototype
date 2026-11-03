"""
Beginner Voice Assistant Prototype
Features:
- Microphone voice input
- Hello greeting
- Current time and date
- Google web search
- Text-to-speech responses
- Friendly handling when speech is not understood
"""

import datetime
import webbrowser
import urllib.parse

import speech_recognition as sr
import pyttsx3


def setup_speaker():
    """Create and configure the text-to-speech engine."""
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)
    return engine


speaker = setup_speaker()


def speak(message):
    """Print and speak every assistant response."""
    print(f"Assistant: {message}")
    speaker.say(message)
    speaker.runAndWait()


def listen():
    """Listen to one microphone command and convert it to text."""
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening... Speak now.")
            recognizer.adjust_for_ambient_noise(source, duration=0.6)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You: {command}")
        return command.lower().strip()

    except sr.WaitTimeoutError:
        speak("I did not hear anything. Please try again.")
    except sr.UnknownValueError:
        speak("Sorry, I could not understand that. Please repeat.")
    except sr.RequestError:
        speak("Speech recognition service is unavailable. Please check your internet connection.")
    except OSError:
        speak("I cannot access your microphone. Please check that it is connected and allowed.")
    except Exception as error:
        print(f"Microphone error: {error}")
        speak("Something went wrong while listening. Please try again.")

    return ""


def handle_command(command):
    """Match the recognized words to a beginner-level action."""
    if not command:
        return True

    if "hello" in command or "hi" == command:
        speak("Hello! I am your voice assistant. How can I help you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")

    elif "date" in command or "today" in command:
        current_date = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today's date is {current_date}.")

    elif command.startswith("search for "):
        topic = command.replace("search for ", "", 1).strip()
        if topic:
            speak(f"Searching Google for {topic}.")
            url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(topic)
            webbrowser.open(url)
        else:
            speak("Please tell me what you want to search for.")

    elif command.startswith("search "):
        topic = command.replace("search ", "", 1).strip()
        if topic:
            speak(f"Searching Google for {topic}.")
            url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(topic)
            webbrowser.open(url)
        else:
            speak("Please tell me what you want to search for.")

    elif "exit" in command or "stop" in command or "goodbye" in command:
        speak("Goodbye! Have a great day.")
        return False

    else:
        speak("Sorry, I did not understand that command. Please try again.")

    return True


def main():
    speak("Voice assistant is ready. Say hello, ask for the time or date, or say search followed by a topic. Say stop to exit.")

    running = True
    while running:
        command = listen()
        running = handle_command(command)


if __name__ == "__main__":
    main()
