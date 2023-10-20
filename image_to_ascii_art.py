from PIL import Image  # important image processing

image_path = "sss.jpg" # set your image path

img = Image.open(image_path) # open your image 

# resizeing the image

width, height = img.size

aspect_ratio = height/width

new_width = 120

new_height = aspect_ratio * new_width * 0.35

img = img.resize((new_width, int(new_height)))

# convert image to greyscale format

img = img.convert('L') 

# getting pixels 

pixels = img.getdata()

# replace each pixel with a character from array

chars = ["(",")","#","&","@","$","%","*","\\",":","/"]

new_pixels = [chars[pixel//25] for pixel in pixels]

new_pixels = ''.join(new_pixels)

# split string of chars into multiple strings of length equal to new width and create a list

new_pixels_count = len(new_pixels)

ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]

ascii_image = "\n".join(ascii_image)

# output on console 

# note increase console length to see proper output

print(ascii_image)
