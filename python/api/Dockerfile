FROM python:latest


RUN apt update -y && apt install -y python-pip python-dev

#RUN apt install -y --no-install-recommends gunicorn xvfb wget libnss3 libxss1 libappindicator1 libindicator7 libsdl1.2-dev fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libgtk-3-0 libnspr4 libnss3 libxtst6 lsb-release xdg-utils
WORKDIR /usr/bin
RUN mkdir /certs
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app
COPY gunicorn.conf.py /etc/


WORKDIR /app
EXPOSE 5000

CMD ["/app/start.sh"]
