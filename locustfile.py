from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task
    def panorama400(self):
        self.client.get("/c/400/default/panorama.jpg")

    @task
    def hoch800(self):
        self.client.get("/s/800/default/hoch.jpg")

    @task
    def quer1200(self):
        self.client.get("/l/1400/default/quer.jpg")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "http://localhost:8000"
    min_wait=10
    max_wait=100