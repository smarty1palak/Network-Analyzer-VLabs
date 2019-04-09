from locust import HttpLocust, TaskSet, task
from locust import events
import globalfile as gf

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        gf.i=gf.i+1

    @task(1)
    def index(self):
        with open('codepart.txt') as f:
            content = f.read().splitlines()
        self.client.get(content[gf.i])
    


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000


