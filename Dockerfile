FROM python:3.10.0-alpine

RUN mkdir webscraping-email
WORKDIR webscraping-email


COPY main.py /webscraping-email
COPY src /webscraping-email/src
COPY requirements.txt /webscraping-email

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Set the entry point
CMD ["python", "main.py"]

