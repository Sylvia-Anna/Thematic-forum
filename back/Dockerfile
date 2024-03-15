FROM ubuntu:22.04
WORKDIR /our_project/back/
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3.11

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 80
CMD [ "python3", "views.py" ]

