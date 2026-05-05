import redis
from src.resources.base_resource import BaseResource


class RedisResource(BaseResource):
    def __init__(self, host='localhost', port=6379, db=0):
        self.name = "Redis"
        self.host = host
        self.port = port
        self.db = db
        self.client = None

    def connect(self):
        try:
            self.client = redis.Redis(host=self.host, port=self.port, db=self.db)
            return self.client
        
        #     return self.client.ping() and super().connect() + f" at {self.host}:{self.port}"
        #     return super().connect() + f" at {self.host}:{self.port}"
        #     # Test connection
        #     self.client.ping()
        #     return f"Successfully connected to {self.name} at {self.host}:{self.port}"
        except redis.ConnectionError as e:
            return f"Failed to connect to {self.name}: {str(e)}"
        
    def health_check(self):
        if self.client is None:
            return f"{self.name} client not initialized"
        try:
            self.client.ping()
            return f"{self.name} is healthy!"
        except redis.ConnectionError:
            return f"{self.name} is not healthy!"