FROM python:3.11-slim

WORKDIR /

COPY app.py ./

RUN pip install flask requests

EXPOSE 3000

CMD ["python", "app.py"]