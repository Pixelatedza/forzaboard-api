FROM python:3.9-slim
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "forzaboard.wsgi",  "-b", "0.0.0.0:8000"]
