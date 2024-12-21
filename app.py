import streamlit as st
import speech_recognition as sr

def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Speak now...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        st.write("You said:", text)

    except sr.UnknownValueError:
        st.write("Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        st.write(f"Could not request results from Google Speech Recognition service; {e}")

# Streamlit app
st.title("Speech-to-Text App")

if st.button("Start Recording"):
    transcribe_speech()
