def convert_time(hour, minute, period):
    if period == "am":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    
    return f"{hour:02d}{minute:02d}"


print(convert_time(12, 15, "am"))  
print(convert_time(8, 30, "pm"))  




def two_numbers_positive(a,b,c):
    if (a>0 and b>0 and c<0 )or(a>0 and b<0 and c>0 )or(a<0 and b>0 and c>0) or (a>0 and b<0 and c>0 ):
        return True
    else:
        return False
    

print(two_numbers_positive(2,4,-3))
print(two_numbers_positive(-4,6,8))
print(two_numbers_positive(4,-6,9))
print(two_numbers_positive(-4,6,0))
print(two_numbers_positive(4,6,10))
print(two_numbers_positive(-14,-3,-4))

# def costant_value(word):
#     alphabets={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
#               'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
#               't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
#     alphas={c.lower(): alphabets[c.lower()] for c in word if c not in "aeiou,."}
#     alpha_sum_values=[alphas[key]for key in alphas]
#     return sum(alpha_sum_values)

# print(costant_value("zodiacs"))
# print(costant_value("strength"))


# def constant_value(word):
#     vowels = "aeiou"
#     consonant_substrings = [''.join(substring) for substring in word.split(x) for x in vowels if x in word]

#     alphabet_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
#                        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
#                        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

#     max_value = max(sum(alphabet_values[c] for c in substring) for substring in consonant_substrings)
#     return max_value

# # Examples
# print(constant_value("zodiacs"))  
# print(constant_value("strength")) 

def constant_value(word):
    # Function to get the value of a substring of consonants
    def get_consonant_value(substring):
        alphabet_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                           'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
                           't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        value = sum(alphabet_values[letter] for letter in substring)
        return value

    # Remove vowels and split into consonant substrings
    consonant_substrings = []
    current_substring = ''
    vowels = "aeiou"
    for letter in word:
        if letter not in vowels:
            current_substring += letter
        else:
            if current_substring:
                consonant_substrings.append(current_substring)
                current_substring = ''
    if current_substring:
        consonant_substrings.append(current_substring)

    # Calculate values of consonant substrings and find the maximum value
    max_value = 0
    for substring in consonant_substrings:
        substring_value = get_consonant_value(substring)
        if substring_value > max_value:
            max_value = substring_value

    return max_value

#  test Examples
print(constant_value("zodiacs"))  
print(constant_value("strength"))  


    