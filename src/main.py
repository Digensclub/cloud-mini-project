from fastapi import FastAPI
import uvicorn
from src.resources.redis_resource import RedisResource
from src.resources.prometheus_resource import PrometheusResource

# Initialize FastAPI app
app = FastAPI()

# Initialize resources
redis_resource = RedisResource()
r = redis_resource.connect()

prometheus_resource = PrometheusResource(app)
prometheus_resource.connect()

@app.get("/")
def read_root():
    # Increment a counter in Redis
    r.incr("hits")
    return {
        "message": "Hello, World from FastAPI with Redis and Prometheus!",
        "hits": int(r.get("hits"))
    }

# Optional: only for running directly with `python main.py`
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
