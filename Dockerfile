# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.8.2
COPY . /my_project
WORKDIR /my_project
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
