# syntax=docker/dockerfile:1

FROM python:3.10-bullseye AS builder
RUN mkdir /e7gvgbot
COPY . /e7gvgbot
WORKDIR /e7gvgbot
RUN apt update
RUN apt-get install sudo apt-get install make automake gcc g++ subversion python3-dev libxml2-dev libxslt1-dev
ENV VIRTUAL_ENV=/e7gvgbot/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3 -m pip install --upgrade pip
RUN pip install wheel
RUN pip install -r /e7gvgbot/requirements.txt

FROM python:3.10-alpine
RUN mkdir /e7gvgbot
WORKDIR /e7gvgbot
COPY --from=builder /e7gvgbot ./
RUN chmod +x /e7gvgbot
ENV VIRTUAL_ENV=/e7gvgbot/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
CMD ["python3", "./bot.py"]