import argparse

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
    required=True,
    type=int,
    help="Integer key used to shift characters in the cipher (e.g., a shift of 3 in the alphabet means 'A' becomes 'D')",
)
parser.add_argument("--decrypt", action="store_true", help="Decrypt instead of encrypt")

args = parser.parse_args()


def main(original_text, key, decrypt):
    new_text = ""
    if decrypt:
        key *= -1

    for character in original_text:
        if not character.isalpha():
            continue
        else:
            new_text += shift_letter(letter=character, offset=key)
    return new_text


if __name__ == "__main__":
    print(main(args.text, args.key, args.decrypt))
