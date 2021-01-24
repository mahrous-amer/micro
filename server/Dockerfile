FROM python:latest

WORKDIR /server

COPY . /server

RUN pip3 install -r requirements.txt

EXPOSE 9898

CMD ["python3","app.py"]
