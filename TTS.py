apikey = 'bnBJyyNR6mvNnri5oYEbhMV7Wy9lggw2nSkdeecnycsl'
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/e241dd40-55ec-4330-8e21-be95fe1656f2'

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

with open('./TTS_output.mp3', 'wb') as audio_file:
    res = tts.synthesize('Hello World!', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
