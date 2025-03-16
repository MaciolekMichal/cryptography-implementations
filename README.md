# Cryptography implementations

The `ciphers/` directory contains implementations of various cryptographic ciphers.

## Requirements
* Python 3.x

## Currently available ciphers
### Shift Cipher
The `shift_cipher.py` script implements a shift cipher, also known as a Caesar cipher. It encrypts and decrypts text by shifting each letter a fixed number of positions down the alphabet.

#### Usage

The script is run from the command line and takes the following arguments:

*   `--text`: The text to be encrypted or decrypted. (Required)
*   `--key`: The integer key used for the shift. A positive key shifts letters forward; a negative key shifts them backward. (Required)
*   `--decrypt`: A flag that, when present, tells the script to decrypt instead of encrypt. (Optional)

#### Examples

**1. Encrypting text:**

To encrypt the text "hello" with a key of 3:

```bash
python shift_cipher.py --text "Hello world!" --key 3
# returns "khoorzruog"
```

**2. Decrypting text:**

To decrypt the text `khoorzruog`:
```bash
python shift_cipher.py --text "khoorzruog" --key 3 --decrypt
# returns "helloworld"
```

or you could alternatively run:
```bash
python shift_cipher.py --text "khoorzruog" --key -3
# also returns "helloworld" 
```

## Contributing
Contributions are welcome! If you'd like to add more ciphers or improve existing implementations, please feel free to open a pull request.
