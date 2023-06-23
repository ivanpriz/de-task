FROM ubuntu:20.04 as base

RUN apt-get -y update && apt-get -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa && apt-get update &&\
  apt-get install python3.10 -y

RUN apt-get -y install openjdk-8-jdk
RUN apt-get -y install python3.10-distutils &&\
    apt-get -y install python3-apt
# Installing pip for 3.10
RUN apt-get -y install curl
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10

# Setting default python
#RUN update-alternatives --install /usr/bin/python python3 /usr/bin/python3.10 1
#RUN update-alternatives --config python3
#RUN update-alternatives  --set python3 /usr/bin/python3.10

WORKDIR /home/app

ENV PYTHONUNBUFFERED=1

ADD requirements.txt .
ADD jars .
RUN python3.10 -m pip install --no-cache-dir -r requirements.txt

FROM base as final
ADD . .

CMD ["python3.10", "entrypoint.py"]
