def shift_letter(letter, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    original_idx = alphabet.index(letter.lower())
    new_idx = original_idx + offset
    wrapped_idx = new_idx % len(alphabet)

    return alphabet[wrapped_idx]
