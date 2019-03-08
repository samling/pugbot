FROM python:3.6.8-stretch

ADD . .

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]
