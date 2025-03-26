nList = list()

while True:
    n = input('Enter Number: ')
    if n.lower() == 'done': break
    n = float(n)
    nList.append(n)

print('Average: ', sum(nList)/len(nList))
