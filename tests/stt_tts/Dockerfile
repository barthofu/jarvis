FROM python:3.6-slim-stretch

WORKDIR /jarvis-app

# Install pip requirements
RUN apt-get update
RUN apt-get --assume-yes install libpulse-dev pulseaudio swig gcc portaudio*
RUN python -m pip install -r requirements.txt

CMD ["python", "stt.py"]
