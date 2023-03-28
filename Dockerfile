# start from basic alpine python
FROM python:3-alpine
LABEL org.opencontainers.image.source = "https://github.com/quickpipes/bittext"

EXPOSE 5000
RUN mkdir -p /bittext
WORKDIR /bittext

# Dependecies could change or get upgraded occasionally.
COPY requirements.txt ./

# Install dependencies
# gcc libc-dev linux-headers are libs and tools for uwsgi building
# clear not required data at the end to reduce image size
RUN set -e; \
  apk add --no-cache --virtual .build-deps \
  gcc \
  libc-dev \
  linux-headers \
  ; \
  pip install --no-cache-dir -r requirements.txt; \
  apk del .build-deps;

# Your code is changing frequently, place it as last to prevent creation of new layer stack
COPY . .

# this will be executed by docker when you run the image
CMD ["/usr/local/bin/uwsgi", "--ini-paste", "/bittext/uwsgi.ini"]
