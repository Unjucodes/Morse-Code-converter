# Making a Morse code converter

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

# User input
before_converted = input("Enter a message to convert to Morse Code: ").strip().upper()

# List to store Morse code values
morse_code_list = []

# Loop through each character in the input
for char in before_converted:
    if char in morse_code_dict:
        morse_code_list.append(morse_code_dict[char])

converted_message = " ".join(morse_code_list)
print(f"Converted Message: {converted_message}")
input("")