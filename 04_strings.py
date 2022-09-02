a = "Adnan's Book is on the table"
b = 'Adnan"s Book is on the table'
c = '''Adnan's and Adnan"s Book is on the table'''

# String Slicing
# ---------------------

intro = "Hi! Iam " # H->[0],i->[1],!->[2],<space>->[3],I->[4],a->[5],m->[6]
pName = "Adnan"
# String Concatination
fullIntro = intro + pName
# print(fullIntro)
# Character of a specific Index
# print("Index 0 contains", intro[0], "Char")
# print("Index 1 contains", intro[1], "Char")
# print("Index 2 contains", intro[2], "Char")
# print("Index 3 contains", intro[3], "Char")
# print("Index 4 contains", intro[4], "Char")
# print("Index 5 contains", intro[5], "Char")
# print("Index 6 contains", intro[6], "Char")
# print("Index 0 to 6 contains", intro[0:7])
# print("Index 0 to 6 contains", intro[:7])
# print("Index 0 to 6 contains", intro[0:])
# print("Step", pName[0:7:2])
# print("Step", pName[7::-2])

# Sting is immutable (Cannot be changed)
# str1 = "This is an appla"
# str1[14]="a" 

#-------------------------------------------
# 
# String Functions

# print("Length of greeting is", len(fullIntro))
# print(fullIntro.upper())
# print("greeting in LowerCase =>", fullIntro.lower())
# print("check if greeting ends with =>", fullIntro.endswith("Adnan"))
# print("Count No.of times Char. is repeated =>", fullIntro.count("n"))
# print("Capitalise greeting  =>", fullIntro.capitalize())
# print("Find index of character in greeting =>", fullIntro.find("Adnan"))
# print("Replace characters in greeting =>", fullIntro.replace("Adnan", "Human"))

# Escape Sequence
# str = 'Adnan\'s book is new. \n Adnan\"s phone is switched off \t Dry ' 
# print(str)