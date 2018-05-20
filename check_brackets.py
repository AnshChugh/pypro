# python3
'''
Finally It works after so many days... it almost made me quit programming lol
Now I will Reward me with couple of games of PUBG(mobile version in emulator)
'''

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    position = []
    for i, char in enumerate(text):
        if char in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(char)
            position.append(i)

        if char in ")]}":
            # Process closing bracket, write your code here
            try:
                if not are_matching(opening_brackets_stack[-1], char):
                    return i + 1
                else:
                    opening_brackets_stack.pop()
                    position.pop() 
            except IndexError:
                return i + 1
    if position:
        return position[-1] + 1
    return False


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == False:
        print("Success") # Use capital 'S' It broke it every time lol
    else:
        print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
