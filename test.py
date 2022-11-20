f = open('result.txt', 'r')
for line in f:
    print(line)
    if line.split()[1] == 'Обработка':
        print(line.split()[0], line.split()[1])
    
