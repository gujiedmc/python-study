# from redis import StrictRedis
import redis
if __name__=="__main__":
    # 创建StrictRedis对象，与redis服务器建⽴连接
    # sr = StrictRedis()  #不需要密码连接Redis
    #host = '127.0.0.1'为服务器IP, port = 6379为端口号, password = 'topsky'为密码,
    # decode_responses = True，db=3为数据库
    # sr = StrictRedis(host = 'bit.local', port = 6379, password = '',decode_responses = True)
    r = redis.Redis(host="bit.local", port=6379, password="")

    #
    index = 0
    key = 'setRandomTest'
    while index < 100:
        r.sadd(key, index)
        index = index + 1
        print(index)
    else:
        # 循环内部代码未执行break, 即没有触发合适的条件
        print("while循环体未执行break")

    index = 0
    while index < 100:
        print(r.spop(key))
        index+=1