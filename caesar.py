import string

words = ["ASSURANCE", "CYBERSECURITY", "INFINITY", "SAMPLING", "MORNING", "EXAMINATION", "MASTER",
         "SYSTEM", "VISUAL STUDIO", "BACHELOR OF SCIENCE IN INFORMATION TECHNOLOGY"]
encrypted = []

l = list(string.ascii_uppercase)
s = 3
nl = []

def main():
    shift = 0
    for i in range(0, len(l)):
        if i < len(l)-s:
            nl.append(l[i])
        else:
            nl.insert(shift, l[i])
            shift += 1
        
    for word in words:
        temp = ""
        for i in range(0, len(word)):
            if word[i] != ' ':
                temp += l[nl.index(word[i])]
            else:
                temp += ' '
        encrypted.append(temp)
        
    print("-----------------------------------------------------------")
    for i in range(0, len(encrypted)):
        print(f"PLAINT TEXT: {words[i]} >>> ENCRYPTED TEXT: {encrypted[i]}")
        print("-----------------------------------------------------------")
main()