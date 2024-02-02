import string

words = ["ASSURANCE", "CYBERSECURITY", "INFINITY", "SAMPLING", "MORNING", "EXAMINATION", "MASTER",
         "SYSTEM", "VISUAL STUDIO", "BACHELOR OF SCIENCE IN INFORMATION TECHNOLOGY"]
encrypted = []

cipher = text_list = [
    "mqqupmjto", "tyeopqotupbry", "bjdbjbry", "qmilgbjs", "ikpjbjs",
    "oxmibjmrbkj", "imqrop",
    "qyqroi",
    "vbqumg qruhbk",
    "emtaogkp kd qtbojto bj bjdkpimrbkj rotajkgksy"
]


l = list(string.ascii_uppercase)
kw = "METHODS"
nkw = ""
nl = l.copy()

def main():
    add_kw()
    new_alphas()
    encrypt()
    print("-----------------------------------------------------------")
    for i in range(0, len(encrypted)):
        print(f"PLAINT TEXT: {words[i]} >>> ENCRYPTED TEXT: {encrypted[i]}")
        print("-----------------------------------------------------------")
    #test()
    
def add_kw():
    global nkw
    for c in kw:
        if c not in nkw:
            nkw += c

def new_alphas():
    for i in range(0, len(nkw)):
        if nkw[i] in nl:
            nl.remove(nkw[i])
        nl.insert(i, nkw[i])
        
def encrypt():
    for word in words:
        temp = ""
        for c in word:
            if c != ' ':
                temp += nl[l.index(c)]
            else:
                temp += ' '
        encrypted.append(temp)

def test():
  for i in range(0, len(encrypted)):
    if encrypted[i] == cipher[i].upper():
      print(True)
    else:
      print(False)

if __name__ == "__main__":
    main()