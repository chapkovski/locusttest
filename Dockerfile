FROM python:3.7

COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

COPY docker_start.sh docker_start.sh
RUN chmod +x docker_start.sh

EXPOSE 8089 5557 5558

ENTRYPOINT ["./docker_start.sh"]