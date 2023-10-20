letterC = False
letterO = False
letterN = False
word = ""
cmd = input()
while cmd != "End":
    if "a" <= cmd <= "z" or "A" <= cmd <= "Z":
        if not letterC and (cmd == "c" or cmd == "C"):
            letterC = True
        elif not letterO and (cmd == "o" or cmd == "O"):
            letterO = True
        elif not letterN and (cmd == "n" or cmd == "N"):
            letterN = True
        else:
            word += cmd
        if letterC and letterO and letterN:
            print(word, end=" ")
            letterC = False
            letterO = False
            letterN = False
            word = ""
    cmd = input()

