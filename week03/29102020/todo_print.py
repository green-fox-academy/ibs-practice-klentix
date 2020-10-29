# Add "My todo:" to the beginning of the todoText
# Add " - Download games" to the end of the todoText
# Add " - Diablo" to the end of the todoText but with indention

# Expected output:

# My todo:
#  - Buy milk
#  - Download games
#      - Diablo

str0 = 'My todo: \n'
todoText = " - Buy milk\n"
str1 = ' - Download games\n\t'
str2 = ' - Diablo'
print(str0+todoText+str1+str2)


