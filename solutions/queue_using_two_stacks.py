""" Queues: A Tale of Two Stacks """

class MyQueue(object):
    def __init__(self):
        self.elements = list()

    def peek(self):
        if self.elements:
            return self.elements[0]

    def pop(self):
        if self.elements:
            popped_element = self.elements[0]
            self.elements = self.elements[1:]

    def put(self, value):
        self.elements.append(value)


def main():
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


if __name__ == '__main__':
    main()
