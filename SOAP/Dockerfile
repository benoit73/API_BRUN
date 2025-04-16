FROM python:3.10
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt update && apt install -y git
RUN git clone --single-branch --branch SOAP https://github.com/benoit73/API_BRUN.git /api || (cd /api && git pull)
WORKDIR /api/SOAP
RUN pip install Flask psycopg2-binary flask-jsonrpc psycopg2 spyne lxml werkzeug
RUN pip install python-dotenv
CMD ["flask", "run", "--debug"]