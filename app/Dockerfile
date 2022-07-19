FROM python:latest
ADD . /app
WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:app/"
RUN pip install -r requirements.txt
