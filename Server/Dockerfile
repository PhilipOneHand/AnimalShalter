
FROM python:latest
#WORKDIR /app

ADD /requirements.txt app/requirements.txt
RUN pip install -r app/requirements.txt

COPY /Server.py /app/app.py
COPY /templates/ /app/templates/

CMD ["python", "-u", "app/app.py"]
