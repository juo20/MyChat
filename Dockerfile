FROM python:3.9.6-alpine

WORKDIR /app

RUN apk update && apk upgrade && apk add git gcc musl-dev python3-dev libffi-dev openssl-dev cargo postgresql-libs postgresql-dev bash

COPY . ./

RUN pip install --upgrade pip &&  pip install -r requirements.txt

# Has to be commented out as it depends on the postgre db
# that is started up in the compose file

EXPOSE 8000 5432
ENV PYTHONUNBUFFERED=1

#CMD ["python3", "manage.py", "migrate"]
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
