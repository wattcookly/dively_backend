FROM python:3.6-alpine
ENV LIBRARY_PATH=/lib:/usr/lib 
RUN mkdir /app && \
    apk --update add \
    zlib-dev git gcc musl-dev \
    linux-headers bind-tools curl nginx && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h &&\

    rm -rf /var/cache/apk/* && \
    chown -R nginx:www-data /var/lib/nginx
ADD nginx /

WORKDIR /app
ADD . /app/
RUN pip3 install -r requirements.txt

EXPOSE 80
ENTRYPOINT ["/init"]
CMD []