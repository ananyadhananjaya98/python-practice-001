
string1 ="ANANAYgdhjw"
newstring =[]
for i in string1:
    if i.islower():
        newstring.append(i.upper())
    else:
        newstring.append(i.lower())

print("".join(newstring))
