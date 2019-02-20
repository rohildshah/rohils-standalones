import time
norm = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "*"]
back = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
print("This is a program that will encode, or decode your message.")
print("To encode/decode, type your message below.")
print("Keep in mind that all punctuation marks will be left the same.")
print("Type the * symbol at the end of the message.")
msg = input("Type Message: ")
ls = list(msg)
ls2 = list(msg)
a = 0
numb = 0
while a == 0:
    if ls[numb] in norm:
        if ls[numb] == "a":
            ls2[numb] = "z"
        if ls[numb] == "b":
            ls2[numb] = "y"
        if ls[numb] == "c":
            ls2[numb] = "x"
        if ls[numb] == "d":
            ls2[numb] = "w"
        if ls[numb] == "e":
            ls2[numb] = "v"
        if ls[numb] == "f":
            ls2[numb] = "u"
        if ls[numb] == "g":
            ls2[numb] = "t"
        if ls[numb] == "h":
            ls2[numb] = "s"
        if ls[numb] == "i":
            ls2[numb] = "r"
        if ls[numb] == "j":
            ls2[numb] = "q"
        if ls[numb] == "k":
            ls2[numb] = "p"
        if ls[numb] == "l":
            ls2[numb] = "o"
        if ls[numb] == "m":
            ls2[numb] = "n"
        if ls[numb] == "n":
            ls2[numb] = "m"
        if ls[numb] == "o":
            ls2[numb] = "l"
        if ls[numb] == "p":
            ls2[numb] = "k"
        if ls[numb] == "q":
            ls2[numb] = "j"
        if ls[numb] == "r":
            ls2[numb] = "i"
        if ls[numb] == "s":
            ls2[numb] = "h"
        if ls[numb] == "t":
            ls2[numb] = "g"
        if ls[numb] == "u":
            ls2[numb] = "f"
        if ls[numb] == "v":
            ls2[numb] = "e"
        if ls[numb] == "w":
            ls2[numb] = "d"
        if ls[numb] == "x":
            ls2[numb] = "c"
        if ls[numb] == "y":
            ls2[numb] = "b"
        if ls[numb] == "z":
            ls2[numb] = "a"
        if ls[numb] == "*":
            a = 1
            break
        numb = numb + 1
    else:
      numb = numb + 1
      continue
finmsg = ('').join(ls2[0:])
print(finmsg)
