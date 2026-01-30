from fastapi import FastAPI

app = FastAPI()

@app.get("/api/hello")
def hello_world():
    return {"message": "Hello,  fastWorld!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
