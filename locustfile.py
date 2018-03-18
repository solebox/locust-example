from locust import Locust, TaskSet, task
import subprocess
from locust import events

def my_success_handler(request_type, name, response_time, response_length, **kw):
    print("Successfully fetched: %s" % (name))

class MyTaskSet(TaskSet):
    @task
    def my_task(self):
        ret = subprocess.Popen(["/bin/curl", "http://localhost:5000/"])
        events.request_success += my_success_handler
        print("executing my_task")

class MyLocust(Locust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000

