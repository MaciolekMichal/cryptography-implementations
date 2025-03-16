import argparse
import string

from utils import shift_letter

parser = argparse.ArgumentParser(description="Shift Cipher")

parser.add_argument(
    "--text",
    required=True,
    type=str,
    help="The input text that will be encrypted or decrypted using the shift cipher.",
)
parser.add_argument(
    "--key",
    type=int,
    help="Integer key used to shift characters in the cipher (e.g., a shift of 3 in the alphabet means 'A' becomes 'D')",
)
parser.add_argument("--decrypt", action="store_true", help="Decrypt instead of encrypt")
parser.add_argument("--attack", action="store_true", help="Try to decrypt without the key")

args = parser.parse_args()

# Argument validation
if args.decrypt and args.attack:
    parser.error("The --decrypt and --attack flags cannot be used together.")

if args.key is None and not args.attack:
    parser.error("The --key argument is required unless --attack is specified.")


def encrypt(original_text, key):
    new_text = ""

    for character in original_text:
        if not character.isalpha():
            continue
        else:
            new_text += shift_letter(letter=character, offset=key)
    return new_text


def attack(original_text):
    alphabet = string.ascii_lowercase

    print("One of the below 26 plaintext instances is the decrypted message:")

    for potential_key in range(len(alphabet)):
        print(encrypt(original_text, potential_key * -1), end="\n\n")


if __name__ == "__main__":
    if args.decrypt:
        print(encrypt(args.text, args.key * -1))
    elif args.attack:
        attack(args.text)
    else:
        print(encrypt(args.text, args.key))
