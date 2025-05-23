import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# Initialize the engine
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Sorry, I'm having trouble with the speech service.")
    return ""

def respond(query):
    if "time" in query:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "search" in query:
        speak("What do you want to search for?")
        query = listen()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Here are the results for {query}")

    elif "wikipedia" in query:
        speak("Searching Wikipedia...")
        topic = query.replace("wikipedia", "").strip()
        try:
            summary = wikipedia.summary(topic, sentences=2)
            speak(summary)
        except:
            speak("Sorry, I couldn't find anything on Wikipedia.")

    elif "stop" in query or "exit" in query:
        speak("Goodbye!")
        exit()

    else:
        speak("I'm not sure how to help with that.")

# Main loop
speak("Hello, how can I assist you?")
while True:
    command = listen()
    if command:
        respond(command)
