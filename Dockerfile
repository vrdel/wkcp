FROM python:3.14-slim

LABEL org.opencontainers.image.authors=daniel.vrcic@gmail.com

ARG TZ=UTC
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=${TZ}

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install curl tzdata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN curl -L "https://github.com/jgm/pandoc/releases/download/3.6/pandoc-3.6-1-amd64.deb" -o /tmp/pandoc.deb
RUN apt-get install -y /tmp/pandoc.deb

RUN groupadd user -g 1000 && useradd -u 1000 -g 1000 user -m -d /home/user -s /bin/bash

RUN python3 -m venv /opt/wkcp/
RUN /opt/wkcp/bin/python -m pip install --upgrade pip
COPY *.whl /home/user/
RUN bash -c 'source /opt/wkcp/bin/activate && pip install /home/user/*.whl'

USER user
ENTRYPOINT ["/opt/wkcp/bin/wkcp"]
