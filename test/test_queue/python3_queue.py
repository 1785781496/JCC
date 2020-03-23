import queue

def test_quene():
    q = queue.Queue(4)
    print("queue is empty? {}".format(q.empty()))
    print("queue is full? {}".format(q.full()))
    q.put("1")
    q.put("2")
    q.put_nowait("3")
    # block when queue is empty
    q.put("4")
    print("queue is empty? {}".format(q.empty()))
    print("queue is full? {}".format(q.full()))
    print("get first element in queue:{}".format(q.get()))
    print("queue is full? {}".format(q.full()))
    print("get first element in queue:{}".format(q.get_nowait()))
    print("size of the queue :{}".format(q.qsize()))
    help(q.task_done)




if __name__ == '__main__':
    test_quene()