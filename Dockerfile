FROM python:3.9.6-alpine

WORKDIR /app

RUN apk update && apk upgrade && apk add git gcc musl-dev python3-dev libffi-dev openssl-dev cargo postgresql-libs postgresql-dev

COPY . ./

RUN pip install --upgrade pip &&  pip install -r requirements.txt

RUN python3 manage.py migrate
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

CMD [ "python3", "./MyChat/manage.py", "runserver", "0.0.0.0:8000" ]
