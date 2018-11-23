# Use an official Python runtime as a parent image
FROM python:3.6.7-alpine

#Set the working directory
WORKDIR /vmn-python-django-app

# Copy the current directory contents into the container at /vmn-python-django-app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

# Run manage.py when the container launches
CMD ["sh","-c", "python app/manage.py runserver"]


