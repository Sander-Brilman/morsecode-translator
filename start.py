import morseTranslatoin

text = input("What text do you want to translate? ")

text = text.lower() # normalize

allowedChars = [".", "-", "/", " "]

parsedText = ""

for char in text:
    if (char in allowedChars):
        parsedText += char

morsecode = morseTranslatoin.translate(parsedText)

print(f"The translation of '{parsedText}' is: {morsecode}")