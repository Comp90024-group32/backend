FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "backend.py","-port",'443']
