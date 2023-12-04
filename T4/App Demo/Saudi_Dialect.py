import streamlit as st
import pandas as pd
import numpy as np
import random
from io import StringIO
# import sounddevice as sd
from scipy.io.wavfile import write
import Post_Tweet
from klaam import SpeechRecognition
from gtts import gTTS
import mishkal.tashkeel
import speech_recognition as sr
import torchvision.models as models
# from transformers import AutoTokenizer, AutoModelForSequenceClassification, BertForSequenceClassification

# model_path_name = 'bert_model_with_info.pth'
# # model = torch.load(model_path_name)
# model = BertForSequenceClassification.from_pretrained(model_path_name, num_labels=3)
def main(): 
    try:

        if st.button('publish the campaign'):
            Post_Tweet.post_tweet({"text": tweet}) 
        # Audio
        st.header('_Clasify_ by Audio!', divider='rainbow')
        link_audio = st.text_input('link audio to classify')
        '''
        st.info("Or")
        if st.button('Record Audio'):
            # Record the audio
            # Sampling frequency
            freq = 44100

            # Recording duration
            duration = 5

            # Start recorder with the given values 
            # of duration and sample frequency
            recording = sd.rec(int(duration * freq), 
                            samplerate=freq, channels=1)

            # Record audio for the given number of seconds
            sd.wait()

            # This will convert the NumPy array to an audio
            # file with the given sampling frequency
            file_audio = write("recording0.wav", freq, recording.astype(np.int16))

            ## Render the Audio
            audio_file = open('recording0.wav', 'rb')
            audio_bytes = audio_file.read()

            st.audio(audio_bytes, format='audio/wav')

            sample_rate = 44100  # 44100 samples per second
            seconds = 2  # Note duration of 2 seconds
            frequency_la = 440  # Our played note will be 440 Hz
            # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
            t = np.linspace(0, seconds, seconds * sample_rate, False)
            # Generate a 440 Hz sine wave
            note_la = np.sin(frequency_la * t * 2 * np.pi)

            raw_audio = st.audio(note_la, sample_rate=sample_rate)
        '''
        if st.button('Speech Recongnition'):
            r = sr.Recognizer("ar-SA")
            with sr.WavFile("recording0.wav") as source:              # use "test.wav" as the audio source
                audio = r.record(source)                        # extract audio data from the file

            try:
                st.write("Transcription: " + r.recognize(audio))   # recognize speech using Google Speech Recognition
            except LookupError:                                 # speech is unintelligible
                st.write    ("Could not understand audio")

            if not link_audio:
                st.warning('Please enter audio link or Youtube link:', icon="⚠️")
            else:
                st.write('اللهجة المدخلة هي:', random.choice(classes))
            if not open('recording0.wav', 'rb'):
                st.warning('Please record the audio:', icon="⚠️")
            else:
                model = SpeechRecognition()
                model.transcribe("recording0.wav")
    except Exception as ee:
        print("Error", ee)


if __name__=="__main__": 
    main() 