from fastapi import FastAPI # type: ignore
from app.data import guide_steps, fashion_news, fashion_brands, communities

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Fashion Trends Guide API"}

@app.get("/steps")
def get_steps():
    return {"steps": guide_steps}

@app.get("/news")
def get_news():
    return {"news": fashion_news}

@app.get("/brands")
def get_brands():
    return {"brands": fashion_brands}

@app.get("/communities")
def get_communities():
    return {"communities": communities}
