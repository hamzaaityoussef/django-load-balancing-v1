# Use Python 3.9 as the base image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run Gunicorn to serve the Django application
CMD ["gunicorn", "django_load_balancing.wsgi:application", "--bind", "0.0.0.0:8000"]