from flask import json
import redis

r = redis.Redis(host="localhost", port=9001, db=0)
sample = {"id": 3, "url": "http://example.com"}
r.lpush("mylist", json.dumps(sample))
