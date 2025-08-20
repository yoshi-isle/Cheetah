import os
from flask import json
import redis
from urllib.parse import urlparse

redis_url = os.getenv("REDIS_CONNECTION_STRING", "redis://localhost:6379")
parsed_url = urlparse(redis_url)
r = redis.Redis(host=parsed_url.hostname, port=parsed_url.port, db=0)

while True:
    _, message = r.brpop("mylist")
    data = json.loads(message)
    print(f"Processing message: {data}")
    pass
