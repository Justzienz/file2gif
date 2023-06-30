# file2gif

file2gif is a Python program that allows you to encrypt any file and turn it into a gif file. It consists of two files: `encrypt.py` and `decrypt.py`.

## Usage

Clone and move to this repository.

```bash
git clone https://github.com/Justzienz/file2gif/
cd file2gif
```

To encrypt a file and turn it into a gif, run the `encrypt.py`. It will ask for the file path. The file must be one of the following types: zip, png, or txt (more file types will be added if you request).

```bash
python encrypt.py
```

The program will convert the file into a sequence of white and black pixels, and save it as a series of 608x608 images in the `images` folder. If any pixel remains unused, they will be turned into red pixels to tell the decrypter when yo stop. Then, it will combine all the images into a single gif file named `crypted.gif`.

To decrypt the `crypted.gif` file and recover the original file, run the `decrypt.py` script. It will ask for the original file's format (zip, png or txt).

```bash
python decrypt.py
```

The decrypted file will be saved in the current folder.

## Requirements

- Python 3.x
- Pillow library (you can install it using `pip install Pillow`)
- imageio library (you can install it using `pip install imageio`)

## Example

Here's an example of how to use file2gif to encrypt a `zip` file:

```bash
python encrypt.py
```

This will create a `crypted.gif` file in the main folder. To decrypt the `crypted.gif` file and recover the original `zip` file, run:

```bash
python decrypt.py
```

The decrypted file will be saved in the main folder.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
