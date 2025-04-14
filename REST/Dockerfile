FROM python:latest
WORKDIR /api
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt update && apt install -y git
RUN pip install Flask psycopg2 flask-swagger-ui
RUN git clone -b REST https://github.com/benoit73/API_BRUN.git /api || (cd /api && git pull)
CMD ["flask", "run", "--debug"]