FROM python:latest
#WORKDIR /app

# Set the environment variables
ENV MYSQL_HOST=db
ENV MYSQL_PORT=3306
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=pass1234
ENV MYSQL_DATABASE=Animal_Shelter

ADD Server/requirements.txt app/requirements.txt
RUN pip install -r app/requirements.txt

COPY Server/Server.py /app/app.py
COPY Server/templates/ /app/templates/

CMD ["python", "-u", "app/app.py"]