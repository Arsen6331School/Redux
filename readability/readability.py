def calcIndex(words, letters, sentences):
    return (0.0588 * ((letters / words) * 100) - (0.296 * (sentences / words) * 100)) - 15.8


text = input("Text: ")

words = 1
letters = 0
sentences = 0
for char in text:
    if char.isalpha():
        letters += 1
    elif char.isspace():
        words += 1
    elif char in [".", "!", "?"]:
        sentences += 1

index = calcIndex(words, letters, sentences)

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print("Grade", round(index))
