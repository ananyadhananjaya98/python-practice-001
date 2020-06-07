def minion_game(s):
    kevin_score, stuart_score =0,0
    for i in range(len(s)):
        if s[i] in list("AEIOU"):
            kevin_score+= len(s)-i
        else:
            stuart_score+= len(s)-i
    if kevin_score> stuart_score:
        print("Kevin ",kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart ",stuart_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
