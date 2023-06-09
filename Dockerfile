FROM python:latest

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]

