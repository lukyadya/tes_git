from locust import TaskSet, HttpUser, constant, task

class test_2(TaskSet):   
    @task 
    def get_500_status(self):
        self.client.get("/500")
        print("Berhasil mendapatkan code 500")

    @task 
    def get_status(self):
        self.client.get("/200")
        print("Berhasil mendapatkan code 200")

class test_1(HttpUser):
        host = "https://partaiperindo.com"
        tasks = [test_2]
        wait_time = constant(1)