def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']

# Returns count of vowels in str
def countVowels(str):
    count = 0
    for i in range(len(str)):
        # Check for vowel
        if isVowel(str[i]):
            count += 1
    return count

# str = 'dev'
# print(countVowels(str))
a = countVowels("DEV")
print(a)
