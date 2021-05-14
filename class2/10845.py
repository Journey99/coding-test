from collections import deque
import sys

queue = deque()


def push(X):
    queue.append(X)


def pop():
    pop_value = 0
    if queue:
        pop_value = queue.popleft()
        print(pop_value)
    else:
        print(-1)


def size():
    if queue:
        print(len(queue))
    else:
        print(0)


def empty():
    if queue:
        print(0)
    else:
        print(1)


def front():
    if queue:
        print(queue[0])
    else:
        print(-1)


def back():
    if queue:
        print(queue[-1])
    else:
        print(-1)


N = int(sys.stdin.readline())

for i in range(N):
    String = list(map(str, sys.stdin.readline().split()))

    if String[0] == 'push':
        push(String[1])
    elif String[0] == 'pop':
        pop()
    elif String[0] == 'size':
        size()
    elif String[0] == 'empty':
        empty()
    elif String[0] == 'front':
        front()
    else:
        back()