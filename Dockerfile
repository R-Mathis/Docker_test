FROM python:3.9.5

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./Testing.py /code/

# 
CMD ["python", "Testing.py"]
