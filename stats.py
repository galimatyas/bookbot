def count_words(text):
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def count_letters(text):
    letter_counts = {}
    for letter in text.lower():
        if letter.isalpha():
             if letter not in letter_counts:
                 letter_counts[letter] = 1
             else:
                 letter_counts[letter] += 1
    return letter_counts

def sort_letter_counts(letter_counts):
    letters = [{"char": k, "num": v} for k, v in letter_counts.items()]
    letters.sort(key=lambda x: x["num"], reverse=True)
    return letters


