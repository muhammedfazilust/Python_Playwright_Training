def count_char(st):
    vowels = consonants = digits = spaces = 0

    for char in st:
        if char.isspace():
            spaces+=1
        elif char.isdigit():
            digits+=1
        elif char.isalpha():
            if char.lower() in 'aeiou':
                vowels+=1
            else:
                consonants+=1

    return vowels, consonants, digits, spaces

text = 'Python 123'
vowels, consonants, digits, spaces = count_char(text)
print(f"vowels:{vowels}, consonants:{consonants}, digits:{digits}, spaces:{spaces}")