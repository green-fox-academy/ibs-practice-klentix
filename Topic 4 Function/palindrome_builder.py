def palindrome(word):
    new_word = word[::-1]
    return (word + new_word)
print(palindrome('car'))


def palsearch(word):
    for i in word:

            if word == word[::-1]:
                print("it's a palindrome")
            else:
                print("not a palindrome")

(palsearch('nepalapen'))