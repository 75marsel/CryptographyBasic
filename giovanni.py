import string

words = ["ASSURANCE", "CYBERSECURITY", "INFINITY", "SAMPLING", "MORNING", "EXAMINATION", "MASTER",
         "SYSTEM", "VISUAL STUDIO", "BACHELOR OF SCIENCE IN INFORMATION TECHNOLOGY"]
encrypted = []

l = list(string.ascii_uppercase)
kw = "METHODS"
kl = 'C'
nkw = ""
nl = l.copy()

def add_kw():
    global nkw
    for c in kw:
        if c not in nkw:
            nkw += c

def new_alphas():
    index = l.index(kl) # index of key letter
    backtrack, skip = 0, 0
    
    for i in range(0, len(nkw)):
      nl.remove(nkw[i]) # remove keyword letter from the new list
      nl.insert(index+i, nkw[i]) # insert it at the index of key letter + i
      
    lk_index = nl.index(nkw[-1]) + 1
    
    for i in range(0, len(l)):
      if not (l[i] in nkw):
        try:
          nl[lk_index + i - skip] = l[i]
        except:
          nl[backtrack] = l[i]
          backtrack += 1
      else:
        skip += 1

def encrypt():
    for word in words:
        temp = ""
        for c in word:
            if c != ' ':
                temp += nl[l.index(c)]
            else:
                temp += ' '
        encrypted.append(temp)
  
def main():
  add_kw()
  '''print(f"""
    KEYWORD: {kw} length: {len(kw)}
    NEW KEYWORD: {nkw} length: {len(nkw)}
    KEY LETTER: {kl}
    """)
  '''
  
  new_alphas()

  encrypt()
  print("-----------------------------------------------------------")
  for i in range(0, len(encrypted)):
      print(f"PLAINT TEXT: {words[i]} >>> ENCRYPTED TEXT: {encrypted[i]}")
      print("-----------------------------------------------------------")
  #print(encrypted)

if __name__ == "__main__":
  main()