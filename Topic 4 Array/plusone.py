def substr(str,keyword):
    for i in range(0,len(str) - len(keyword)):
        for j in range (0, len(keyword)):
            if str[i+j] != keyword[j]:
                break
            elif j == len(keyword) - 1:
                print(i)

if __name__ == '__main__':
    substr("this is what i'm searching for","search")