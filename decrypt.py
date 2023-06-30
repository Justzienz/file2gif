from PIL import Image

def get_frames_from_gif(gif_path):
  frames = []
  try:
    image = Image.open(gif_path)
  except IOError:
    print(f"Error opening file: {gif_path}")
    return frames
  n_frames = 0
  while True:
    try:
      image.seek(n_frames)
      frame = image.copy()
      frames.append(frame)
      n_frames += 1
    except EOFError:
      break
  return frames 

def get_bin(image):
  width,height = image.size
  binary = ""
  flag = True
  for x in range(width):
    if flag:
      for y in range(height):
        if image.getpixel((y,x)) == 2:
          binary += "0"
        elif image.getpixel((y,x)) == 0:
          binary += "1"
        else:
          flag = False
  return binary

def bin2png(binary):
  binary_data = bytes(int(binary[i:i+8], 2) for i in range(0, len(binary), 8))
  with open("decrypted.png", "wb") as f:
    f.write(binary_data)
def bin2txt(binary):
  binary_data = int(binary, 2).to_bytes((len(binary) + 7) // 8, byteorder='big')
  with open("decrypted.txt", "wb") as f:
    f.write(binary_data)
def bin2zip(binary):
  with open("decrypted.zip", "wb") as f:
    for i in range(0, len(binary), 8):
      byte = int(binary[i:i+8], 2)
      f.write(chr(byte).encode('latin-1'))
      
gif_path = "crypted.gif"
frames = get_frames_from_gif(gif_path)

binary = ""
for image in frames:
  binary += get_bin(image)

method = input("Bin to Text: b2t\nBin to PNG: b2png\nBin to zip: b2z\nChoose a method: ")
if method == "b2t":
  bin2txt(binary)
elif method == "b2png":
  bin2png(binary)
elif method == "b2z":
  bin2zip(binary)
else:
  print("You didn't choose a right method.")
