import redis

class redis_client:
    def __init__(self,host='localhost', port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db);

    def set_value(self,key,value):
        self.r.set(key,value);

    def get_value(self,key):
        return self.r.get(key);

    def get_allkeys(self):
        return self.r.scan();

    def hexists(self,key,item):
        flag = self.r.hexists(key,item);
        return flag

    def hset(self,key,item,value):
        return self.r.hset(key,item,value);
