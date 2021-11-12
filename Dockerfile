# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /e7chatbot

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./ .

RUN python3 bot.py