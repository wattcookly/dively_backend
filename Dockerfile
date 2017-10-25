FROM python:3.5-alpine
ENV LIBRARY_PATH=/lib:/usr/lib
RUN mkdir /app && \
    apk --update add git gcc musl-dev
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
