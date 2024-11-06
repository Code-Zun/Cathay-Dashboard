from fastapi import FastAPI
#from .api.endpoints import flight_data, competitor_analysis, pricing

app = FastAPI(title="Airline Competitive Analysis API")

# app.include_router(flight_data.router)
# app.include_router(competitor_analysis.router)
# app.include_router(pricing.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)