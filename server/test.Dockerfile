FROM python:3.9

RUN mkdir -p /usr/src/app 
WORKDIR /usr/src/app

COPY ./requirements2.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements2.txt


ENV PYTHONPATH=/usr/src/app


ENTRYPOINT ["/bin/bash"]
