#check character is in uppercase or lower case

char=input("enter the charcater:")
if char.isupper():
    print(char," is upper case character")
elif char.islower():
    print(char," is lower case character")
else:
    print("it is not an alphabet")