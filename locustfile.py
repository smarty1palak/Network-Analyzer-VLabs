from locust import HttpLocust, TaskSet, task
from locust import events
from additional_handlers import additional_success_handler, additional_failure_handler

# events.request_success += additional_success_handler
# events.request_failure += additional_failure_handler

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """

    @task(1)
    def index(self):
        self.client.get("/")



class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

