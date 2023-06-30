from PIL import Image, ImageDraw
import math
import subprocess
import os
import imageio.v2 as imageio

file = input("Give the file name: ")

#remove any remaining images
subprocess.run("rm images/*", shell=True)

#get binaries of the file
with open(file, "rb") as f:
  binary_data = f.read()
binary = ''.join(format(byte, '08b') for byte in binary_data)

color1 = (0, 0, 0)
color2 = (255, 255, 255)
color3 = (255, 0, 0)
palette = [color1,color2,color3]
index, slide = 0,0

while index < len(binary):
  slide += 1
  img = Image.new('P', (608, 608), color=0)
  img.putpalette([c for color in palette for c in color])
  for x in range(608):
    for y in range(608):
      try:
        if binary[index] == "1":
          img.putpixel((y,x), 1)
      except IndexError:
        img.putpixel((y,x), 2)
      index += 1
  img.save(f'images/image{slide}.png')
print("Images generated!")

gif_name = 'crypted.gif'

images = [img for img in os.listdir("images") if img.endswith('.jpg') or img.endswith('.png')]
images.sort()

fps = 1
writer = imageio.get_writer(gif_name, duration=fps)

for image in images:
  writer.append_data(imageio.imread(os.path.join("images", image)))

writer.close()

print("Gif generated!")
