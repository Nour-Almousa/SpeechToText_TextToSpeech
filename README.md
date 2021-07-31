# SpeechToText_TextToSpeech

In this repository, you will see:

* A live transcription of speech to a text using IBM Watson Speech to Text service and saving the output in a .txt file.
* Written text conversion to audio using IBM Watson Text to Speech service and saving the output as a .mp3 file.

## Steps Followed for Speech Transcription (STT):
1. Setting up the service: from the IBM Cloud website, create the service with the Lite Plan.
2. Clone the code of Live STT  provided by IBM on https://github.com/IBM/watson-streaming-stt
3. Installing dependencies that are pyaudio and websocket-client.
4. Updating the credentials in speech.cfg with credentials I got when setting up the service.
5. Adding a 3-lines code to transcribe.py that saves the output in STT_output.txt.
6. Running Live transcription code.

## Steps Followed for Text to Speech conversion (TTS):
1. Installing dependencies: ibm_watson and import TextToSpeechV1 and IAMAuthenticator.
2. Setting up the service: from the IBM Cloud website, create the service with the Lite Plan.
3. Creating authenticator instance and pass the API key.
4. Creating an instance of the text to speech service and pass the authenticator.
5. Setting the service URL.
6. Saving the text as audio in TTS_output.mp3.
