# Predefined strings for encoding and decoding
PREFIX = "Cb^r@1-xWesq"  # Prefix string for encoding
SUFFIX = "Xb!d0p!aa-0*1z"  # Suffix string for encoding


def encode_message(message):
    """
    Encodes a message by adding PREFIX and SUFFIX to each word with more than 2 characters,
    and reverses words with fewer than 3 characters.
    """
    coded_message = []

    for word in message.split():
        if len(word) >= 3:
            # Add PREFIX and SUFFIX for encoding
            encoded_word = PREFIX + word + SUFFIX
        else:
            # Reverse the word for encoding
            encoded_word = word[::-1]

        coded_message.append(encoded_word)

    return " ".join(coded_message)


def decode_message(message):
    """
    Decodes a message by removing PREFIX and SUFFIX from each encoded word,
    and reversing words with fewer than 3 characters.
    """
    coded_message = []

    for word in message.split():
        if word.startswith(PREFIX) and word.endswith(SUFFIX):
            # Remove PREFIX and SUFFIX to decode
            decoded_word = word[len(PREFIX):-len(SUFFIX)]
        else:
            # Reverse the word to decode
            decoded_word = word[::-1]

        coded_message.append(decoded_word)

    return " ".join(coded_message)


def main():
    """
    Main function to handle user interaction for encoding, decoding, and quitting.
    """
    while True:
        # Prompt the user to choose an action
        command = input("\nEnter the Command Number:\n"
                        "1 to Encode\n"
                        "2 to Decode\n"
                        "3 to Quit\n> ")

        if command == '3':
            print('\nProgram Exited!')
            break

        if command not in ('1', '2'):
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        # Get the message from the user
        message = input("Enter the Text: ")

        if command == '1':
            # Encode the message
            print("The Encoded Text is:", encode_message(message))

        elif command == '2':
            # Decode the message
            print("The Decoded Text is:", decode_message(message))


if __name__ == "__main__":
    main()
