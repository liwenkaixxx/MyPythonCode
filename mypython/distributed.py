import random,time,Queue
from multiprocessing.managers import BaseManager

# 第一步：建立task_queue和result_queue，用来存放任务和结果
task_queue = Queue.Queue()
result_queue = Qeue.Queue()

class Queuemanager(BaseManager):
    pass

# 第二步：吧创建的队列注册在网络上，
# 利用register方法，callable参数关联了queue对象
#将queue对象在网络上暴露
Queuemanager.register('get_task_queu',callable = lambda:task_queue)
Queuemanager.register('get_result_queue',callable = lambda:result_queue)

# 第三步：绑定端口8001，设置验证口令‘qiye’。这个相当与初始化
manager = Queuemanager(address=('',8001),authkey='qiye')

# 第四步：启动管理，监听信息通道
manager.start()

# 第五步：通过管理实例的方法获得通过网络访问Queue对象
task = manager.get_task_queu()
result = manager.get_result_queu()

# 第六步：添加任务
for url in ["ImageUrl_"+i for i in range(10)]:
    print 'put task %s...'%url
    task.put(url)

# 获得返回结果
print('try get result...')
for i in range(10):
    print 'result is %s'%result.get(timeout = 10)

# 关闭管理

manager.shutdown()


