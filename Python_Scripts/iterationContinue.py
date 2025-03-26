while True:
    line = input('> ')
    if line[0] == '#':
        continue #this will sent the control to the while statement i.e. line 1
    elif line == 'Done':
        break
    print(line)
print('Done!')
