
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': '/'
}


REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('')
    return ' '.join(morse_code)


def morse_to_text(morse_code):
    words = morse_code.split(' / ')
    decoded_text = []

    for word in words:
        letters = word.split()
        decoded_word = ''.join([REVERSE_MORSE_CODE_DICT[letter] for letter in letters])
        decoded_text.append(decoded_word)

    return ' '.join(decoded_text)


message = "PYTHON 3"
morse_message = text_to_morse(message)
print(f"'{message}' в коде Морзе: {morse_message}")

decoded_message = morse_to_text(morse_message)
print(f"Декодировано обратно: {decoded_message}")
