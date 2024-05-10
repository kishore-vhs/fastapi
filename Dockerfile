FROM python:3.11
LABEL app="BOTO3 with FASTAPI"
MAINTAINER developed='hemasivakishore'
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt \
    && python --version
COPY main.py main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]