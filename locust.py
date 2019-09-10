from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    @task(1)
    def list_post(self):
        headers = {'content-type': 'application/json', 'Accept-Encoding': 'gzip'}
        a = self.client.post("/model/parse",
                             headers=headers,
                             name="access nlu",
                             data='{"text":"hello"}')

        print(a.status_code)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
