FROM python:3.10.8
WORKDIR /app

RUN apt-get -y update
RUN apt-get -y install vim nano

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /app
CMD [ "python", "app.py" ]