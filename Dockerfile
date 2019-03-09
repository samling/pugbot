FROM python:3.6.8-stretch

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

RUN cp /usr/share/zoneinfo/America/Los_Angeles /etc/localtime

CMD [ "python", "main.py" ]
