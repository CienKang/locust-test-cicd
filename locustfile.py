from locust import HttpUser, TaskSet, task, between
import random

class UserTasks(TaskSet):
    @task(1,name="Get all Users")
    def get_all_users(self):
        self.client.get("/users")

    @task(2)
    def get_user(self, name="Get some Users"):
        user_id = random.randint(1, 2)  # Assuming we have 2 users with IDs 1 and 2
        self.client.get(f"/users/{user_id}")

    @task(3,name="Create a new user")
    def create_user(self):
        new_user = {
            "name": f"User {random.randint(3, 100)}",
            "email": f"user{random.randint(1, 100)}@example.com"
        }
        self.client.post("/users", json=new_user)

    @task(4)
    def update_user(self, name="Update a user"):
        user_id = random.randint(1, 2)
        updated_user = {
            "name": f"Updated User {random.randint(1, 100)}",
            "email": f"updated_user{random.randint(1, 100)}@example.com"
        }
        self.client.put(f"/users/{user_id}", json=updated_user)

class WebsiteUser(HttpUser):
    tasks = [UserTasks]
    wait_time = between(1, 3)  # Wait time between tasks (1 to 3 seconds)
