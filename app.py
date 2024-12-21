import streamlit as st
import speech_recognition as sr
import tempfile
import os

# Streamlit app title
st.title("Speech-to-Text Tool")

st.write("Click the button below to record your speech and see it transcribed.")

# Button to start recording
if st.button("Start Recording"):
    st.write("Recording... Speak into your microphone.")
    
    # Use the SpeechRecognition library to capture audio
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            # Adjust for ambient noise and record audio
            recognizer.adjust_for_ambient_noise(source, duration=1)
            st.write("Listening...")
            audio = recognizer.listen(source, timeout=5)

            # Transcribe speech to text
            st.write("Processing your speech...")
            text = recognizer.recognize_google(audio)
            st.success(f"Transcription: {text}")

        except sr.UnknownValueError:
            st.error("Sorry, I couldn't understand the audio. Please try again.")
        except sr.RequestError as e:
            st.error(f"Error with the Speech Recognition service: {e}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
