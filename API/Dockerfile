FROM python:3.11-slim 

WORKDIR /

COPY app.py ./

RUN pip install flask redis

EXPOSE 5000

CMD ["python", "app.py"]