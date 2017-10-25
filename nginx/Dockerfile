FROM alpine:3.4
MAINTAINER Kowit C. <kowit@cookly.me`>
ADD root /
ENV S6_OVERLAY_VERSION=v1.17.2.0
RUN apk add --no-cache bind-tools && \
    apk add --no-cache curl && \
    curl -sSL https://github.com/just-containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz \
    | tar xfz - -C / && \
    apk del curl && \
    apk add --update nginx && \
    rm -rf /var/cache/apk/* && \
    chown -R nginx:www-data /var/lib/nginx

EXPOSE 80
ENTRYPOINT ["/init"]
