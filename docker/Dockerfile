FROM python:3.11.12-slim 

RUN apt-get update
RUN apt install -y postgresql

RUN mkdir /autoria-task

WORKDIR /autoria-task

COPY req.txt .

RUN pip install -r req.txt
RUN playwright install --with-deps firefox

COPY . .

RUN chmod a+x /autoria-task/docker/*.sh

CMD ["python", "-m", "src.main"]