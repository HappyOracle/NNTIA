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
text = "моя киска хочет тебя. Я родилась, что сосать твой член. Я хотела, чтобы ты кончал мне внутрь и оплодворил меня. " \
       "Я вчера увидела, как ты открыто изменяешь и жестко трахаешь официантку. " \
       "У меня жестко текла киска, что я не могла простить тебя за измену, но хотела чтобы ты также жестко трахнул." \
       " Я не могу перестать думать о тебе и о сексе. Потому что, я живу ради твоего члена. Я умру без члена. " \
       "Благодаря твоей сперме я живу. Выеби меня, ах, пожалуйста трахни меня. Пока ты спишь, я снимаю трусики и дрочу перед тобой." \
       " Когда ты писаешь, у меня слюнки текут. Когда ты ходишь, я кончаю." \
       "Я ради тебя побрила все и почистила свою киску. Когда ты войдешь ком мне внутрь, ты почувствуешь весь мое тепло к тебе." \
       " Моя влага даст тебе расслабиться. Я готова ходить голой где угодно, и когда угодно. Используй меня как в туалет." \
       " Трахни меня, писай на меня, дрочи на меня. Я твоя мастурбаторша"
#text = "Я анимешник и я дед инсайд, я люблю смотреть хентай и пикать пуджа когда я мастурбирую" #baya
#text = "Алё, Кирилл,У нас тут свет отключили! Пизда нахуй, пиздец бля" #aidar
#text = "Тыы, отвергааешь, моой даар?! Ии все этии, жаалкиее шаавки, пришлии, увидеть твою смеэрть?"
#text = "блатик, остановис ах, ах, ах, ах, ах, ах, у меня что-то выходит блатик!"


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