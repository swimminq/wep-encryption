S = [x for x in range(0,256)]

K = []
key = "RC4"
text = "Swimming"

# 초기화
def init():
    for i in range(0,256):
        K.append(key[i % len(key)])

    print(K)

# 셔플
def shuffle():
    j = 0
    for i in range(0,256):
        j = (j + S[i]) % 256
        S[i],S[j] = S[j],S[i]

    print(S)

init()
shuffle()
