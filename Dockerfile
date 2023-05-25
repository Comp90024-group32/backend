
FROM python:3.8.8

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "backend.py","-port",'443']
