from os import path

USE_STT = False
USE_TTS = False

# =========== STT ===========

WAKE_UP_WORD = "jarvis"
ACTIVE_ENGINE = "google"

# =========== Directories ===========

SRC_DIR = path.dirname(path.abspath(__file__))

MEDIA_DIR = path.join(SRC_DIR, 'data')
SOUNDS_DIR = path.join(MEDIA_DIR, 'sounds')
KEYPHRASES = path.join(SRC_DIR, 'data/keyphrases.txt')

MODULES_IMPORT_DIR = "src.modules"

# =========== Parser ===========

IGNORE_KEYWORDS = [ 'hey jarvis', ',', 'please', ' the ', ' a ', ' an ', ' can you ' ]
TRESHOLD = 0.6