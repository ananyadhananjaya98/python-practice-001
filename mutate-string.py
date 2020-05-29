def mutate_string(string, position, character):
    x = list(string)
    for i in range(len(x)):
        if i == position:
            x[i] = character
    newstring = "".join(x)
    return newstring

string = input()
pos , char = input().split()

print(mutate_string(string,int(pos),char))

