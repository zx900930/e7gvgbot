# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /e7chatbot

COPY . .
RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]