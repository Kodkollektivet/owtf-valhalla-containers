FROM python:3.5
RUN apt-get update && apt-get -y install nmap
RUN pip install --upgrade pip

ADD . /owtf
WORKDIR /owtf

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]