

class BaseResource:
    def connect(self):
        if hasattr(self, 'name'):
            return f"Connecting to {self.name}..."
        raise NotImplementedError("Subclasses must implement this method")
    
    def health_check(self):
        return f"{self.name} is healthy!" if hasattr(self, 'name') else "Resource name not set"