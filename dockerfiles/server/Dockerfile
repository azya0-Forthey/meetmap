FROM python:3.13-slim

LABEL authors="Forthey"

WORKDIR /server

COPY server/requirements.txt /server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

COPY db.yaml /

COPY server /server

WORKDIR /server/source

#CMD ["fastapi", "run", "main.py", "--port", "8080", "--workers", "4", "--host", "0.0.0.0"]
CMD ["fastapi", "dev" , "main.py", "--port", "8080", "--host", "0.0.0.0"]


# RUN echo 'ping localhost &' > /bootstrap.sh
# RUN echo 'sleep infinity' >> /bootstrap.sh
# RUN chmod +x /bootstrap.sh

# CMD /bootstrap.sh