FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN pip install -r requirements.txt