FROM ubuntu
RUN apt-get update && apt-get install -y \ 
    python3 \
    python3-pip
RUN pip3 install numpy 
COPY main.py .
COPY test2.py .
CMD python3 main.py && python3 test2.py