def reverse_string(text: str) -> str:
    return text[::-1]
def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count
def is_palindrome(text: str) -> bool:
    text = text.lower()
    return text == text[::-1]
word: str = input("Enter a word: ")
print("Reversed:", reverse_string(word))
print("Vowel Count:", count_vowels(word))
print("Palindrome:", is_palindrome(word))