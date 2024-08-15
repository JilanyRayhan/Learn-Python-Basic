name = input("enter a text for vowel counting: ")
vowels = "aeiou"
name = name.casefold()

count = {keys:sum([1 for char in name if char == keys])for keys in vowels}
print(count)