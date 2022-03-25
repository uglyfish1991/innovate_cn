                ################################################
                #                                              #
                #              Activity 1                      #
                #                                              #
                ################################################

def check(message):

    if (len(message)) % 2 ==0:
        print("even")
    else:
        print("odd")

check("Welcome to Code Nation")
check("Hi")
check("Boo")

                ################################################
                #                                              #
                #              Activity 2                      #
                #                                              #
                ################################################

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w","x","y","z"]

for letter in alpha:
    print(letter)

answer = int(input("Please type in a number to see the corresponding letter of the alphabet"))

answer -=1

print(alpha[answer])

                ################################################
                #                                              #
                #              Activity 3                      #
                #                                              #
                ################################################

                #                      WIP                     #

                
s=["","","","","","","","",""]

grid = f"""
----------------------
|      |      |      |
|   {s[0]}   |   {s[1]}    |   {s[2]}    |
|      |      |      |
----------------------
|      |      |      |
|   {s[3]}    |   {s[4]}    |   {s[5]}    |
|      |      |      |
----------------------
|      |      |      |
|   {s[6]}    |   {s[7]}    |   {s[8]}    |
|      |      |      |
----------------------
"""
def player_one():
    global s
    global grid
    ans=int(input("Select a square 1 - 9"))
    s[ans-1] = "x"
    print(f"""
----------------------
|      |      |      |
|   {s[0]}   |   {s[1]}    |   {s[2]}    |
|      |      |      |
----------------------
|      |      |      |
|   {s[3]}    |   {s[4]}    |   {s[5]}    |
|      |      |      |
----------------------
|      |      |      |
|   {s[6]}    |   {s[7]}    |   {s[8]}    |
|      |      |      |
----------------------
""")
player_one()