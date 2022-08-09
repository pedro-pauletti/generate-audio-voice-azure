import azure.cognitiveservices.speech as speechsdk
import json

speech_config = speechsdk.SpeechConfig(subscription="YourSubscriptionKey", region="YourServiceRegion")

with open("data.json", encoding='utf-8') as my_json:
    data = json.load(my_json)

for i in data:
    print(f"Generating the mp3 file called: {i['title']}")
    audio_config = speechsdk.audio.AudioOutputConfig(filename=f"audios/{i['title']}.mp3")
    speech_config.speech_synthesis_voice_name='pt-BR-AntonioNeural'
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    speech_synthesizer.speak_text_async(i['text'])
print("Finished")
