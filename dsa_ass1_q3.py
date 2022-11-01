#Write a program to check if two strings are a rotation of each other?

def Rotations(str1, str2):
    s1 = len(str1)
    s2 = len(str2)
    temp = ''
 
    if s1 != s2:
        return 0
 
    temp = str1 + str1

    if (temp.count(str2) > 0):
        return 1
    else:
        return 0
 
 
if __name__ == "__main__":
    str1 = "AACD"
    str2 = "ACDA"
 
    if Rotations(str1, str2):
        print("Strings are rotations of each other")
    else:
        print("Strings are not rotations of each other")