from locust import HttpUser, TaskSet, task

class MyTask(TaskSet):
    def get_root_path(self):
        self.client.get("/")
    
    @task
    def get_predictions(self):
        self.client.post("/predict")

class MyLocust(HttpUser):
    tasks = [MyTask]
    host = "https://udacity-cicd-capstone.azurewebsites.net"
    min_wait = 1000
    max_wait = 2000
