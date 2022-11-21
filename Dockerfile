FROM python:3.10.8
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /app
CMD [ "python", "app.py" ]