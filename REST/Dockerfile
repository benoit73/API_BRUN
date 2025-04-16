FROM python:latest
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt update && apt install -y git
RUN git clone -b REST https://github.com/benoit73/API_BRUN.git /api || (cd /api && git pull)
WORKDIR /api/REST
RUN pip install Flask psycopg2 flask-swagger-ui
CMD ["flask", "run", "--debug"]