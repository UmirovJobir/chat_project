FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt ./code
COPY . .

# RUN  docker rm $(docker ps -a -q)
# RUN  docker rmi $(docker images -q)

RUN apt-get update \
    && apt-get install -yyq netcat

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

COPY entrypoint.sh .
ENTRYPOINT [ "sh", "./entrypoint.sh" ]