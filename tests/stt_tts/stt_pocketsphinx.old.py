import sys, os, pyaudio
from pocketsphinx import *

p = pyaudio.PyAudio()

KEYWORD = 'jarvis'

print(p.get_device_count())

for i in range(0, p.get_device_count()):
        print("Name: " + p.get_device_info_by_index(i)["name"])
        print("Index: " + str(p.get_device_info_by_index(i)["index"]))
        print("\n")

exit()

modeldir = get_model_path()
# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', os.path.join(modeldir, 'en-us'))
config.set_string('-lm', os.path.join(modeldir, 'en-us.lm.bin'))

config.set_string('-dict', os.path.join(modeldir, 'cmudict-en-us.dict'))
config.set_string('-keyphrase', KEYWORD)
config.set_float('-kws_threshold', 1e-40)

decoder = Decoder(config)
print('spotting')
decoder.start_utt()

stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()        

while True:
    buf = stream.read(1024)
    decoder.process_raw(buf, False, False)
    if decoder.hyp() != None:
        print(decoder.hyp().hypstr)
    if decoder.hyp() != None and decoder.hyp().hypstr == KEYWORD:
        print("Detected keyword, restarting search")
        decoder.end_utt()
        print('spotting')
        decoder.start_utt()