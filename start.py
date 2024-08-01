


text = input("What text do you want to translate?\n\n");

text = text.lower().replace(" ", "");# normalize

allowedChars = "qwweertyuiopoasdfghjklzxcvbnmn1234567890 ";

parsedText = "";

for char in text:
    if (char in allowedChars):
        parsedText += char;

morsecode = "";

print("The translation of " + parsedText + " is: \n\n" + morsecode);