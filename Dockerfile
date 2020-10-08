FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apk --update add \
    build-base \
    jpeg-dev \
    zlib-dev
RUN pip install -r requirements.txt
COPY . /code/
CMD ["python", "manage.py", "runserver"]