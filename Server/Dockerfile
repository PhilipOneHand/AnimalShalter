FROM python:latest
WORKDIR /code

# Set the environment variables
ENV MYSQL_HOST=db
ENV MYSQL_PORT=3306
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=pass1234
ENV MYSQL_DATABASE=Animal_Shelter

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY Server.py /server/app.py
COPY ../templates /templates

CMD ["python", "-u", "app.py"]