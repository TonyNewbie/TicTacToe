vowels = 'aeiou'
# create your list here
string = input()
string_vowels = [vowel for vowel in string if vowel in vowels]
print(string_vowels)
