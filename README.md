# root-me
root-me challenges

## "CAPTCHA me if you can"
```python
docker build -t python_ocr ./
docker run -it -v ${PWD}:/opt -w /opt python_ocr:latest main.py
```
