def longest_word(string1, string2, string3):
    if(len(string1) > len(string2) and len(string1) > len(string3)):
        print string1
    elif(len(string2) > len(string1) and len(string2) > len(string3)):
        print string2
    elif(len(string3) > len(string1) and len(string3) > len(string2)):
        print string3
    else:
        print("They have the same length")

firstString = ""
secondString = ""
thirdString = ""


firstString = raw_input("Enter a String: ")
secondString = raw_input("Enter a String: ")
thirdString = raw_input("Enter a String: ")

longest_word(firstString,secondString,thirdString)
