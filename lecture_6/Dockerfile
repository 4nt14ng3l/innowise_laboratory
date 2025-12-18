# Use the official Python 3.11 slim image as the base
FROM python:3.11-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all remaining application files into the container
COPY . .

# Expose port 8000 to allow external access to the application
EXPOSE 8000

# Define the command to run the FastAPI app using Uvicorn
# - 'main:app' refers to the 'app' instance in the 'main.py' file
# - '--host 0.0.0.0' makes the app accessible from outside the container
# - '--port 8000' sets the port the app will listen on
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
