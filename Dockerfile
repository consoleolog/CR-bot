FROM python:3.10

RUN apt-get update && \
    apt-get install -y pulseaudio portaudio19-dev python3-pyaudio && \
    apt-get install -y alsa-utils && \
    apt install build-essential -y && \
    apt-get install libespeak1 -y && \
    apt-get install mpg321 -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app

COPY ./ /usr/src/app

WORKDIR /usr/src/app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "mike.py"]

#RUN python mike.py
