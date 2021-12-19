FROM python:3.9-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY . /code
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "forzaboard.wsgi",  "-b", "0.0.0.0:8000"]
