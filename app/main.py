from fastapi import FastAPI
from app.interfaces.api.account_controller import router as account_router

app = FastAPI()

# Include API routers
app.include_router(account_router, prefix="/accounts", tags=["accounts"])


@app.get("/")
def read_root():
    """
    Root endpoint to verify the application is running.

    Returns:
        dict: A simple message indicating the API is running.
    """
    return {"message": "Buckpal application is running!"}
