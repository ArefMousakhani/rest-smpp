FROM python:3.8
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./
CMD python service.py