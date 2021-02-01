import random
from locust import HttpUser, TaskSet, task, between
class QuickstartUser(TaskSet):
    wait_time = between(5, 10)
    @task
    def index(self):
        self.client.get("/")
    @task(3)
    def checkPredict(self):
        self.client.post("/predict", json={
            "CHAS":{
                "0":0
            },
            "RM":{
                "0":6.575
            },
            "TAX":{
                "0":296.0
            },
            "PTRATIO":{
                "0":15.3
            },
            "B":{
                "0":396.9
            },
            "LSTAT":{
                "0":4.98
            }
        })

class WebsiteUser(HttpUser):
    task_set = QuickstartUser
    min_wait = 5000
    max_wait = 9000
    host = "https://boston-housing-prediction-flask.azurewebsites.net"
