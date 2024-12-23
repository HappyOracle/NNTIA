import torch
import sounddevice as sd
import time

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'aidar' #aidar, baya, kseniya, xenia, random
put_accent = True
put_yo = True
device = torch.device('cpu')
text = "123"

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                         model='silero_tts',
                         language=language,
                         speaker=model_id,
                         )
model.to(device)

audio = model.apply_tts(text=text,
                        speaker=speaker,
                        sample_rate=sample_rate,
                        put_accent=put_accent,
                        put_yo=put_yo)

#возпроизводим наш терминатор ыхыхыхыхыхыхы
print(text)

#def va_speak(what: str):
#    audio = model.apply_tts(text=what,
#                            speaker=speaker,
#                            sample_rate=sample_rate,
#                            put_accent=put_accent,
#                            put_yo=put_yo)
#    sd.play(audio, sample_rate)
#    sd.wait()
#    sd.stop()

sd.play(audio, sample_rate)
time.sleep( len(audio) / sample_rate)
sd.stop()
