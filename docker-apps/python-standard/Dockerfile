FROM python:3.6

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py", "-p 5000"]

#EXPOSE 80
#CMD ["python", "app.py", "-p 80"]
 