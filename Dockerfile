FROM python:3.12.0a7-alpine3.18
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

ENV FLASK_APP app
ENTRYPOINT ["python3", "backend.py"]
