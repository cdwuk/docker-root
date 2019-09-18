FROM python:3.6
RUN mkdir /app
WORKDIR /app
ADD . /app/
COPY . .
RUN pip install -r requirements.txt
# RUN pip install --upgrade pip
CMD ["python", "app.py", "-p 80"]
 