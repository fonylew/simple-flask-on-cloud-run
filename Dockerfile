FROM python:3.7-slim

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod 444 app.py
RUN chmod 444 requirements.txt
RUN chmod 444 conversion.csv

ENV PORT 8080

# Run the web service on container startup.
CMD [ "python", "app.py" ]