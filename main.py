import sys
import os

sys.path.insert(0, os.path.abspath(__file__ + "/../src"))
sys.path.insert(0, os.path.abspath(__file__ + "/../src/core"))

os.environ['SDL_AUDIODRIVER'] = 'dsp'

from src.core.jarvis import Jarvis

Jarvis().listen()