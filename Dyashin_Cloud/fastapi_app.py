from fastapi import FastAPI

app = FastAPI(title="Docker Container Example")

app.get("/")
async def index():
    return f"Hello world! Welcome to docker"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port="8080")





