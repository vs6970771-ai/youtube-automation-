from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ShortsMaster AI",
    description="YouTube Shorts Automation Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {
        "message": "Welcome to ShortsMaster AI",
        "status": "Running",
        "languages": ["Hindi", "English"],
        "categories": "All Categories"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/categories")
def categories():
    return {
        "categories": [
            "Facts",
            "Mystery",
            "Baby and Family",
            "Comedy",
            "Science",
            "History",
            "Animals",
            "Motivation",
            "Gaming",
            "3D Animation",
            "Education",
            "Entertainment"
        ]
    }
