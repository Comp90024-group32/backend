
FROM python:2.7-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "backend.py","-port",'443']
