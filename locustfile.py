from locust import HttpUser, TaskSet, task, between
import random

class UserTasks(TaskSet):
    @task(1)
    def get_all_users(self):
        self.client.get("/users",name="Get all Users")

    @task(2)
    def get_user(self, name="Get some Users"):
        user_id = random.randint(1, 2)  # Assuming we have 2 users with IDs 1 and 2
        self.client.get(f"/users/{user_id}",name="Get a user")

    @task(3)
    def create_user(self):
        new_user = {
            "name": f"User {random.randint(3, 100)}",
            "email": f"user{random.randint(1, 100)}@example.com"
        }
        self.client.post("/users", json=new_user,name="Create a user ")

    @task(4)
    def update_user(self, name="Update a user"):
        user_id = random.randint(1, 2)
        updated_user = {
            "name": f"Updated User {random.randint(1, 100)}",
            "email": f"updated_user{random.randint(1, 100)}@example.com"
        }
        self.client.put(f"/users/{user_id}", json=updated_user,name="Update a user")

class WebsiteUser(HttpUser):
    tasks = [UserTasks]
    wait_time = between(1, 3)  # Wait time between tasks (1 to 3 seconds)
