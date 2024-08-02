import morseTranslatoin

text = input("What text do you want to translate?\n\n");

text = text.lower().replace(" ", "");# normalize

allowedChars = ".- ";

parsedText = "";

for char in text:
    if (char in allowedChars):
        parsedText += char;

morsecode = morseTranslatoin.translate(parsedText)

print("The translation of " + parsedText + " is: \n\n" + morsecode);