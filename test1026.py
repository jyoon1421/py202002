instruction = int(input())
queue = []
ins = {}

for i in range(instruction):
    ins[i] = input().split(' ')

for i in range(instruction):
    if ins[i][0] == 'push':
        queue.append(int(ins[i][1]))

    elif ins[i][0] == 'pop':
        if len(queue) != 0:
            print(queue.pop(0))
        else: print(-1)

    elif ins[i][0] == 'size':
        print(len(queue))

    elif ins[i][0] == 'empty':
        if len(queue) == 0:
            print(1)
        else: print(0)

    elif ins[i][0] == 'front': # 맨 위 꺼내고 출력, 없으면 -1
        if len(queue) != 0:
            print(queue[0])
        else: print(-1)

    elif ins[i][0] == 'back': # 맨 위 꺼내고 출력, 없으면 -1
        if len(queue) != 0:
            print(queue[-1])
        else: print(-1)
