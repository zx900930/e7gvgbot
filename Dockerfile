# syntax=docker/dockerfile:1

FROM python:3.9-alpine
COPY . /
WORKDIR /
RUN pip install -r requirements.txt
CMD ["python3", "./bot.py"]