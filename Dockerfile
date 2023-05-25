FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine

RUN apk update && apk --no-cache add bash nano

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["/usr/local/bin/python", "backend.py",'--host',"0.0.0.0", "--port", "443"]
