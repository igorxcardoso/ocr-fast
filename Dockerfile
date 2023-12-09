# Use a base image with Python
FROM python:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files to the working directory
COPY requirements.txt /app

# Create and activate a virtual environment
RUN python -m venv venv && \
    . venv/bin/activate

# Install the application dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the remaining files to the working directory
COPY . /app

# Expose port 5000 to the external world, so we can access our application
EXPOSE 5000

# Command to start the application when the container is run
CMD ["python", "run.py"]