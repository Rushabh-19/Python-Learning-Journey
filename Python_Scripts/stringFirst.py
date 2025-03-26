str = "Hello World"

print("Using While loop:\n\n")
x = 0
while x < len(str):
    c = str[x]
    print (x , c)
    x+= 1
print ("\n\nUsing For Loop:\n\n")

for letter in str:
    print (letter)
