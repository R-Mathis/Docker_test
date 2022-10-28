FROM python:3.9
WORKDIR /app
COPY . /app
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
CMD [ "uvicorn" , "Testing:app", "--reload"]
