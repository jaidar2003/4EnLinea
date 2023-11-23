FROM python:3-alpine
LABEL authors="Juan Manuel Aidar"

RUN apk update
RUN apk add git
RUN git clone https://github.com/jaidar2003/4EnLinea.git
WORKDIR /jaidar2003/4EnLinea.git
RUN pip install -r requirements.txt

CMD [ "sh", "-c", "coverage run -m unittest && coverage report -m && python -m game.main" ]