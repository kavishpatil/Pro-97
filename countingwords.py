introString = input("enter your string")
characterCount = 0
wordCount = 1
for i in introString:
    characterCount=characterCount+1
    if(i==" "):
        wordCount=wordCount+1
print("number of words in the given string",wordCount) 
print("number of character in the given string",characterCount)       