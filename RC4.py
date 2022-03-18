S = [x for x in range(0,256)]

K = []
key = "RC4"
text = "Swimming"
KeyStream = []

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

# 암호문과 복호문의 대칭키(KeyStream) 생성
def CreateKey():
    m = 0
    n = 0

    for _ in range(0, len(text)):
        m = (m + 1) % 256
        n = (n + S[m]) % 256
        S[m], S[n] = S[n],S[m]

        t = (S[m] + S[n]) % 256

        KeyStream.append(S[t])
    
    print(KeyStream)


def Encryption():
    count = 0
    crypto = []

    for k in range(0, len(text)):
        crypto.append(ord(text[k]) ^ KeyStream[k])

    print(crypto)

init()
shuffle()
CreateKey()
Encryption()