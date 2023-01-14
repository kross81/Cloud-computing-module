FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=index.py
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install Flask_Cors
RUN pip install flask-response
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
#comments


