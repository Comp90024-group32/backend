FROM python:3.12.0a7-alpine3.18
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 443
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=443
ENV FLASK_APP app
ENTRYPOINT ["python3", "backend.py"]
