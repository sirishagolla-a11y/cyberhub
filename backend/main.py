from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import api_router

app = FastAPI(
    title="CYBERHUB Backend API",
    version="0.1.0",
    description="AI-Powered Public Digital Identity Intelligence System API"
)

# Configure CORS for React frontend development server
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "status": "ok",
        "message": "CyberHub backend is running"
    }

# Include API routes under /api
app.include_router(api_router, prefix="/api")
