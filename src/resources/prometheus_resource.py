from prometheus_fastapi_instrumentator import Instrumentator
from src.resources.base_resource import BaseResource


class PrometheusResource(BaseResource):
    def __init__(self, app):
        self.app = app

        # self.name = "Prometheus"
    def connect(self):
        Instrumentator().instrument(self.app).expose(self.app)
        # return super().connect() + " and Prometheus metrics exposed at /metrics"
    
    def health_check(self):
        return super().health_check()