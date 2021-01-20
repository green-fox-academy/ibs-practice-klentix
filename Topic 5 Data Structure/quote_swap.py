# Accidentally I messed up this quote from Richard Feynman.
# Two words are out of place
# Your task is to fix it by swapping the right words with code

# Also, print the sentence to the output with spaces in between.
# Create a function called quote_swap()

words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."]

def quote_swap(words):
    for i in range(len(words)):
        if words[i] == "do":
            words[i] = "cannot"
        if words[i] == "cannot":
            words[i] = "do"
    sentence = ' '.join(words)
    print(sentence)
print(quote_swap(words))
# Expected output: "What I cannot create I do not understand."


