consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']


vowels = ['a','e','i','o','u']

string1 = input("Enter a word \n")
string1 = string1.lower();
print("You entered : %s" % string1)

if string1[0] in consonants:
    print(string1[1:]+string1[0]+'ay')
elif string1[0] in vowels:
    print(string1+'ay')
else:
    print("Not a word")