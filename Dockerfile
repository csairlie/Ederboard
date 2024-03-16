FROM python:3.9
WORKDIR /usr/src/app
COPY *.py .
RUN pip install --upgrade pip && \
    pip install edapi python-dotenv
CMD ["python", "./main.py"]
