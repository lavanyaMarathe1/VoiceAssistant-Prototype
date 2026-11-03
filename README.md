# Voice Assistant – Beginner Prototype

A simple Python voice assistant that listens through a microphone, recognizes spoken commands, performs basic actions, and speaks every response.

## Features
- Microphone input using `SpeechRecognition`
- Greeting for "Hello" or "Hi"
- Current time and date
- Google search in the default browser
- Text-to-speech using `pyttsx3`
- Friendly handling for silence, unclear speech, internet issues, and microphone errors
- Say "stop", "exit", or "goodbye" to close the assistant

## Requirements
- Windows 10/11 (also adaptable to macOS/Linux)
- Python 3.10–3.12 recommended
- Working microphone and speakers
- Internet connection for Google speech recognition and web searches

## Setup in VS Code (Windows PowerShell)

Open the project folder in VS Code, then open Terminal and run:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, run this once in the current terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

If `PyAudio` fails to install, first confirm you are using Python 3.12:

```powershell
python --version
```

Then try:

```powershell
python -m pip install PyAudio==0.2.14
```

## Run

```powershell
python main.py
```

Speak clearly after the assistant says it is listening.

## Example commands
- "Hello"
- "What is the time?"
- "What is today's date?"
- "Search for Python tutorials"
- "Stop"

## How it works
1. The microphone captures audio.
2. `SpeechRecognition` sends the audio to Google's speech recognition service and receives text. Internet is required.
3. The program checks the recognized text for supported commands.
4. Python performs the action (date/time or opening a Google search).
5. `pyttsx3` speaks the response.

## Notes
- This is a beginner prototype, not a continuously running smart AI assistant.
- Google speech recognition requires an internet connection.
- `pyttsx3` generally works offline for speech output.
- Do not commit your `.venv` folder to GitHub. Add it to `.gitignore`.
