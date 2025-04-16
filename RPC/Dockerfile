FROM python:latest
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt update && apt install -y git
RUN git clone --single-branch --branch RPC https://github.com/benoit73/API_BRUN.git /api || (cd /api && git pull)
WORKDIR /api/RPC
RUN pip install Flask psycopg2-binary flask-jsonrpc psycopg2
RUN pip install python-dotenv
CMD ["flask", "run", "--debug"]