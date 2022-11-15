from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("https://numericalintegrationsahkoun.azurewebsites.net/home/0/3.14")
    
