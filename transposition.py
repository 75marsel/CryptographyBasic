import string

sample = "MEET ME AFTER THE TOGA PARTY"
words = ["ASSURANCE", "CYBERSECURITY", "INFINITY", "SAMPLING", "MORNING", "EXAMINATION", "MASTER",
         "SYSTEM", "VISUAL STUDIO", "BACHELOR OF SCIENCE IN INFORMATION TECHNOLOGY"]
encrypted = []

rail = 1
l = list(string.ascii_uppercase)
nl = []

def rails():
  global fr, sr
  swap = 0

  for word in words:
    for i in range(0, len(word)):
      if word[i] != ' ':
        if len(nl) < rail + 1:
          for j in range(0, rail):
            nl.append(word[i+j])
            i += j
        else:
          if swap > rail:
            swap = 0
          nl[swap] += word[i]
          swap += 1

    encrypted.append(nl.copy())
    nl.clear()

def main():
  rails()
  print("-----------------------------------------------------------")
  for i in range(0, len(encrypted)):
      print(f"PLAINT TEXT: {words[i]} >>> ENCRYPTED TEXT: {encrypted[i]}")
      print("-----------------------------------------------------------")


if __name__ == "__main__":
  main()