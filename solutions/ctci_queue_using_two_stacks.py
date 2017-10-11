""" Queues: A Tale of Two Stacks """

class MyQueue(object):
    def __init__(self):
        
    
    def peek(self):
        
        
    def pop(self):
        
        
    def put(self, value):
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        
