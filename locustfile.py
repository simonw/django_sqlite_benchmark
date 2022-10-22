from locust import HttpUser, task
import itertools
import sqlite3


# Output as dictionaries
sqlite3.enable_callback_tracebacks(True)
db = sqlite3.connect("generated.db")
db.row_factory = sqlite3.Row
rows = (
    dict(r)
    for r in itertools.cycle(
        db.execute("SELECT * FROM rows ORDER BY random()").fetchall()
    )
)


class CounterOne(HttpUser):
    # @task
    # def counter_one(self):
    #     self.client.get("/counter/one/")

    @task
    def write(self):
        self.client.post("/write/", next(rows))
