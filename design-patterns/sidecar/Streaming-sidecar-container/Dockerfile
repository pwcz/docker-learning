FROM python:3.6
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /app
CMD cd /app && waitress-serve --host 0.0.0.0 --port 8000 math_app:api