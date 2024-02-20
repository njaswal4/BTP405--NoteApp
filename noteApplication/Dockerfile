# Use the official Python image as a base image
FROM python:3.9-slim

# Install dependencies
RUN pip install --no-cache-dir mysql-connector-python

# Expose the port on which the server will run
EXPOSE 8000

# Command to run the server
CMD ["python", "Server.py"]
