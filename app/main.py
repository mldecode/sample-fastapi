import logging
from fastapi import FastAPI
from .routes import user
from .database import engine
from .models import user as user_model

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create database tables
user_model.Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management API")

# Include routers
app.include_router(user.router, prefix="/users", tags=["users"])

@app.on_event("startup")
async def startup_event():
    logger.info("Application startup")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown")
