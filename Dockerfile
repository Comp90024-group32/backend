
FROM python:3.12.0a7-alpine3.18
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "backend.py","-port",'443']
