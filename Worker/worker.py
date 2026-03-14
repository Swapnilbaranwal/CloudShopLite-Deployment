import time
import redis
import os

redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379)

while True:
    r.incr("background_jobs")
    print("Worker incremented background_jobs")
    time.sleep(5)