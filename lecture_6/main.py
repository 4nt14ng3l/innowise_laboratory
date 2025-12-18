# Import the FastAPI class to create the application
from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI()

# Define a GET endpoint at the path "/healthcheck"
@app.get("/healthcheck")
async def healthcheck() -> dict:
    # Return a simple JSON response indicating the service is healthy
    return {"status": "ok"}
