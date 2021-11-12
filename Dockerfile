# syntax=docker/dockerfile:1

FROM python:3.9-alpine
RUN mkdir /e7gvgbot
COPY . /e7gvgbot
WORKDIR /e7gvgbot
RUN pip install -r /e7gvgbot/requirements.txt
RUN chmod +x /e7gvgbot
CMD ["python3", "./bot.py"]