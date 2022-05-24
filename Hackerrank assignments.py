
a = int(input())
b = int(input())
print('{0} \n{1} \n{2}'.format((a + b), (a - b), (a * b)))








if __name__ == '__main__':
    N = int(input())
    empty = []
    conv = []

    for i in range(N):
        x = input().split()
        empty.append(x)

    for i in range(len(empty)):
        if empty[i][0] == 'insert':
            x = int(empty[i][1])
            y = int(empty[i][2])
            conv.insert(x,y)
        elif empty[i][0] == 'print':
            print(conv)
        elif empty[i][0] == 'remove':
            conv.remove(int(empty[i][1]))
        elif empty[i][0] == 'append':
            conv.append(int(empty[i][1]))
        elif empty[i][0] == 'sort':
            conv.sort()
        elif empty[i][0] == 'pop':
            conv.pop()
        elif empty[i][0] == 'reverse':
            conv.reverse()








if __name__ == '__main__':
    n = int(input())
    print(*[num+1 for num in range(n)], sep='', end="")




if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    
    for key, value in student_marks.items():
        if query_name == key:
            sum = 0
            count = 0
            for i in value:
                sum += i
                count += 1
            average = sum/count
            print("{:.2f}".format(average))