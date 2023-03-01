import asyncio, redis

def doSubscribe(r:redis, *channel):
    pubsub = r.pubsub()
    pubsub.subscribe(channel)
    message = pubsub.parse_response()
    return message

def doPublish(r:redis, channel, msg):
    res = r.publish(channel, msg)
    print(res)

if __name__=="__main__":
    r = redis.Redis(host="127.0.0.1", port=6379, password="")

    count = 0
    while (count < 9):
        doPublish(r, "test_channel", "msg")
        count = count + 1
        doSubscribe(r, *"test_channel")

