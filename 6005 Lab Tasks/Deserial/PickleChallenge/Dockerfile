FROM python:slim

#Netcat for the Shell
RUN apt-get update && apt-get install -y ncat
ADD serverflag.txt /


WORKDIR /opt

#Copy Files
ADD REQUIREMENTS.txt /opt

#Install Requirements
RUN pip install -r REQUIREMENTS.txt

ADD app.py /opt
ADD templates/* /opt/templates/

CMD ["flask", "run", "--host=0.0.0.0"]
