LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
MORSECODE_ALPHABET = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----"]

def translate(input):
    temp = ""
    arrayOfLetters = input.split(" ")
    for i in range(len(arrayOfLetters)):
        for j in range(len(MORSECODE_ALPHABET)):
            if arrayOfLetters[i] == MORSECODE_ALPHABET[j]:
                temp += LETTERS[j]
    return temp