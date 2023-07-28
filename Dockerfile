FROM ubuntu:latest
WORKDIR .
RUN apt update && apt install python3 python3-pip -y
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["python3","app.py"]
