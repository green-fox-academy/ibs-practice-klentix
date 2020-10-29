telbook = {"William A. Lathan":"405-709-1865",
           "John K. Miller":"402-247-8568",
           "Hortensia E. Foster":"606-481-6467",
           "Amanda D. Newland":"319-243-5613",
           "Brooke P. Askew":"307-687-2982"}

#What is John K. Miller's phone number?
print("John's number:", telbook.get("John K. Miller"))

#Whose phone number is 307-687-2982?
for k,v in telbook.items():
    if '307-687-2982' in v:
        print("number 307-687-2982 belongs to :", k)

#Do we know Chris E. Myers' phone number?
for k,v in telbook.items():
    if 'Chris E. Myers' not in k:
        print("there is no Chris E. Myers phone number")
    break

