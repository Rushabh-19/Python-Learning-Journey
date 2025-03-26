str = input('Please Enter the String: ')
ch = input('Charater to be Count: ')


c = 0
for letter in str:
    if letter == ch:
        c+=1

print("there are %s \'%s\' in word \'%s\'" %(c,ch,str))
