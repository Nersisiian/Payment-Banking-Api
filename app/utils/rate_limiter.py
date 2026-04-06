import redis
import os

r = redis.Redis.from_url(os.getenv("REDIS_URL"))

def is_allowed(key: str, limit=5, window=60):
    current = r.get(key)

    if current and int(current) >= limit:
        return False

    pipe = r.pipeline()
    pipe.incr(key, 1)
    pipe.expire(key, window)
    pipe.execute()

    return True