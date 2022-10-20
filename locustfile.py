from locust import HttpUser, task


class CounterOne(HttpUser):
    @task
    def counter_one(self):
        self.client.get("/counter/one/")
