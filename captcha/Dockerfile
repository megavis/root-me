FROM python:3.8-slim

RUN pip install pytesseract requests
RUN apt-get update -y && \
    apt-get install -y tesseract-ocr && \
    apt-get install -y libtesseract-dev

ENTRYPOINT ["python"]
#CMD["main.py"]
