
FROM python:latest
#WORKDIR /app

ADD Server/requirements.txt app/requirements.txt
RUN pip install -r app/requirements.txt

COPY Server/Server.py /app/app.py
COPY /templates/ /app/templates/

CMD ["python", "-u", "app/app.py"]
