from fastapi import FastAPI
import uvicorn
import redis

# Initialize FastAPI app
app = FastAPI()

# Connect to Redis (global client)
r = redis.Redis(host="localhost", port=6379, db=0)

@app.get("/")
def read_root():
    # Increment a counter in Redis
    r.incr("hits")
    return {
        "message": "Hello, World",
        "hits": int(r.get("hits"))
    }

# Optional: only for running directly with `python main.py`
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
