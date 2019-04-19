FROM python:3.5

COPY ./app /app/

RUN pip install -r requirements.txt

WORKDIR /app/

# If STATIC_INDEX is 1, serve / with /static/index.html directly (or the static URL configured)
ENV STATIC_INDEX 1
# ENV STATIC_INDEX 0

#CMD ["python ./app/app/main.py"]