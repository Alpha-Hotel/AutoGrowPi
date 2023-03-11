FROM python:3.9.16-bullseye

WORKDIR /usr/src/app
RUN apt update -y
RUN apt install -y software-properties-common
RUN apt install -y nginx
RUN apt install -y gunicorn

#RUN add-apt-repository ppa:deadsnakes/ppa
#RUN apt install python3.9

#RUN apt install python3.8-venv
#RUN python3 -m venv ./env
#RUN ./env/Scripts/activate
RUN pip install Django
RUN pip -v

ENV UDEV=1
COPY . ./
# Listen on port 80 for http connections
EXPOSE 80
#CMD ls
#CMD pip show django
CMD python manage.py runserver
#CMD ["./env/Scripts/activate", "&&","gunicorn", "--bind", "0.0.0.0:8000", "PyGrowWebsite.wsgi"]