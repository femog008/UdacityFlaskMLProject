from locust import HttpUser, TaskSet, task
import json

# Loading the test JSON data
with open('test_data.json') as f:
    test_data = json.loads(f.read())
    
class MyTask(TaskSet):
    def get_root_path(self):
        self.client.get("/")
    
    @task
    def get_predictions(self):
        self.client.post("/predict", json = test_data)

class MyLocust(HttpUser):
    tasks = [MyTask]
    host = "https://udacity-cicd-capstone.azurewebsites.net"
    min_wait = 1000
    max_wait = 2000
