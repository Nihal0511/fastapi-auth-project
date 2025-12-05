from fastapi import FastAPI
from app.db import Base, engine
from app.routers import auth, users

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management API")

# Include routers (correct)
app.include_router(auth.router)
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "User Management API running"}
