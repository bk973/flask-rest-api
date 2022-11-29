# Using light weight alpine Image

FROM python:3.10-alpine

#Installing packages

RUN apk update
RUN pip install --no-cache-dir pipenv

#Define Working Directory and adding source code

WORKDIR /user/src/app
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY simple_apis ./simple_apis

#Install all dependencies

RUN pipenv install --system --deploy

#Start the app

EXPOSE 5000
ENTRYPOINT ["user/src/app/bootstrap.sh"]
