# base image  
FROM python:3.8   
# setup environment variable  
ENV DockerHOME=/home/app/webapp  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
# install dependencies  
RUN pip install --upgrade pip  
RUN pip install Django
RUN pip install django-crispy-forms
RUN pip install model_bakery
# copy whole project to your docker home directory. 
COPY . $DockerHOME  
# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD python manage.py runserver  