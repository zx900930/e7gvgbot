# syntax=docker/dockerfile:1

FROM python:3.8-alpine
RUN mkdir /e7gvgbot
COPY . /e7gvgbot
WORKDIR /e7gvgbot
RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
RUN pip install -r /e7gvgbot/requirements.txt
RUN chmod +x /e7gvgbot
CMD ["python3", "./bot.py"]