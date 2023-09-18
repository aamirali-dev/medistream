# Use an official Python runtime as the base image
FROM python:3.8

# Set environment variables for Python and Pipenv
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1

# Create and set the working directory in the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /app/

# Install Pipenv
RUN pip install pipenv

RUN apt-get update && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev

# Install project dependencies using Pipenv
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of the Django project source code to the container
COPY . .

# Expose the port on which your Django app will run (usually 8000)
EXPOSE 8000

# Define the command to start the Django app
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
