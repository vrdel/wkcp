FROM python:3.14-slim

LABEL org.opencontainers.image.authors=daniel.vrcic@gmail.com

RUN apt-get -y update && apt-get -y upgrade

RUN groupadd user -g 1000 && useradd -u 1000 -g 1000 user -m -d /home/user -s /bin/bash

RUN python3 -m venv /opt/wkcp/
RUN /opt/wkcp/bin/python -m pip install --upgrade pip
COPY *.whl /home/user/
RUN bash -c 'source /opt/wkcp/bin/activate && pip install /home/user/*.whl'

USER user
ENTRYPOINT ["/opt/wkcp/bin/wkcp"]
