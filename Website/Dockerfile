FROM python:3.9.16-bullseye

WORKDIR /usr/src/app
COPY . ./
RUN apt update -y
RUN apt install -y nginx
RUN apt install -y gunicorn
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt
RUN pip -v

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 
ENV UDEV=1
COPY . ./
# Listen on port 80 for http connections
#EXPOSE 8000
#CMD python manage.py runserver
#CMD ["./env/Scripts/activate", "&&","gunicorn", "--bind", "0.0.0.0:8000", "PyGrowWebsite.wsgi"]