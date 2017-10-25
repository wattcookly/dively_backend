FROM python:3.6-alpine
ENV LIBRARY_PATH=/lib:/usr/lib \
    S6_OVERLAY_VERSION=v1.20.0.0 \
RUN mkdir /app && \
    apk --update add \
    zlib-dev git gcc musl-dev gettext \
    linux-headers bind-tools curl nginx && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h &&\

    curl -sSL https://github.com/just-containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz \
    | tar xfz - -C / && \

    rm -rf /var/cache/apk/* && \
    chown -R nginx:www-data /var/lib/nginx
ADD nginx /

WORKDIR /app
ADD . /app/
RUN pip3 install -r requirements.txt

EXPOSE 80
ENTRYPOINT ["/init"]
CMD []