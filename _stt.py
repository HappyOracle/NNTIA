import vosk
import sys
import sounddevice as sd
import queue

model = vosk.Model("model") #сам модель 1,5 гб
samplerate = 16000 #синтезатор рекомендуется  8 - 16Hz
device = 1 #id устройства запись (микрофона)

q = queue.Queue()

def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def va_listen(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16', channels=1,
                           callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                print(rec.Result())
            #else:
            #   print(rec.PartialResult())

