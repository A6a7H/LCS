'''
Given a string. Write a program to form a string with first character of all words.
Ex: The bucket is full of water
Output: Tbifow
'''

def sol(strs):
    strs = strs.split()
    new_word = ''
    for word in strs:
        new_word += word[0]
    return new_word

if __name__ == '__main__':
    strs = input()
    print(sol(strs))