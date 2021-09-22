instruction = int(input())
queue = []
command = {}

for i in range(instruction):
    command[i] = input().split(' ')

for i in range(instruction):
    if command[i][0] == 'push':
        queue.append(command[i][1])

    elif command[i][0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))

    elif command[i][0] == 'size':
        print(len(queue))

    elif command[i][0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif command[i][0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif command[i][0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
