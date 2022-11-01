#Q4. Write a program to print the first non-repeated character from a string

str1 = "data science data"
index = -1
fnc = ""
for i in str1:
    if str1.count(i) == 1:
        fnc += i
        break
    else:
        index += 1
if index == 1:
    print("Either all characters are repeating or string is empty")
else:
    print("First non-repeating character is", fnc)