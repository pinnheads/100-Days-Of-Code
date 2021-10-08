codes = {
    "A": "·–",
    "B": "–···",
    "C": "–·–·",
    "D": "–··",
    "E": "·",
    "F": "··–·",
    "G": "––·",
    "H": "····",
    "I": "··",
    "J": "·–––",
    "K": "–·–",
    "L": "·–··",
    "M": "––",
    "N": "–·",
    "O": "–––",
    "P": "·––·",
    "Q": "––·–",
    "R": "·–·",
    "S": "···",
    "T": "–",
    "U": "··–",
    "V": "···–",
    "W": "·––",
    "X": "–··–",
    "Y": "–·––",
    "Z": "––··",
    "1": "·––––",
    "2": "··–––",
    "3": "···––",
    "4": "····–",
    "5": "·····",
    "6": "–····",
    "7": "––···",
    "8": "–––··",
    "9": "––––·",
    "0": "–––––",
    ".": "·–·–·–",
    ",": "––··––",
}


def letter_to_morse(letter: str) -> str:
    """Converts letter to equivalent morse code"""
    letter = letter.upper()
    if letter == " ":
        return " "
    else:
        try:
            return codes[letter]
        except KeyError:
            return letter


def string_to_morse(text: str) -> str:
    """Converts a string to morse code"""
    morse_code = ""
    message = ""
    for word in text:
        message += word + " "
        morse_code += letter_to_morse(word) + " "
    print(f"\n\n{message}\n{morse_code}")
    return morse_code


string_to_morse(input("Enter a String to convert to morse code: "))
