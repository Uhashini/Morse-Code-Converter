# Dictionary to store Morse code of specific characters
morse_code_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',  
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--', 
    '/': '-..-.',  '(': '-.--.',  ')': '-.--.-', '&': '.-...', ':': '---...', 
    ';': '-.-.-.', '=': '-...-',  '+': '.-.-.',  '-': '-....-', '_': '..--.-', 
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

# String input from the user
string = input("String to convert to Morse code: ")

# Convert to Morse code
morse_code = []
for char in string.upper():  # Convert input to uppercase for matching
    if char in morse_code_dict:  # Check if character exists in dictionary
        morse_code.append(morse_code_dict[char])
    elif char == ' ':  # Add a separator for spaces (e.g., between words)
        morse_code.append(' ')  # Optional: customize for word separation
    else:
        print(f"Character '{char}' cannot be converted to Morse code.")

# Print the result
print("Morse Code:", ' '.join(morse_code))

# Dictionary to map Morse code to characters
morse_to_char_dict = {value: key for key, value in morse_code_dict.items()}

# Input Morse code string from user
morse_code = input("Enter Morse code to convert to string (separate with spaces): ")

# Convert Morse code to a string
decoded_message = []
words = morse_code.split("   ")  # Splitting by 3 spaces for word separation
for word in words:
    chars = word.split()  # Splitting by single spaces for character separation
    for char in chars:
        if char in morse_to_char_dict:
            decoded_message.append(morse_to_char_dict[char])
        else:
            print(f"Unknown Morse code: {char}")
            decoded_message.append('?')  # Placeholder for unrecognized codes
    decoded_message.append(' ')  # Add a space to separate words

# Join and print the result
print("Decoded String:", ''.join(decoded_message).strip())
