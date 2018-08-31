from PIL import Image, ImageFile
from math import *

class InvalidNum(Exception):
	print("Try again")

# open the image
# Param: str image_name
# Return: Image object
def load_img(image_name):
    return Image.open(image_name)

#display image
# Param: Image image
# Return: none
def show_img(image):
    image.show()

# save image to computer
# Param: Image image, str name
# Return: none
def save_img(image, name):
    image.save(name + ".jpg", "JPEG")

# applies Obamicon filter
# Param: Image image
# Return: Image
def obamicon(image):
	darkBlue = (0, 51, 76)
	red = (217, 26, 33)
	lightBlue = (112, 150, 158)
	yellow = (252, 227, 166)
	pixels = list(image.getdata())
	new_colors = []
	for each in pixels:
        #each will represent a pixel and pixels have RGB values
		gray_value = (each[0] + each[1] + each[2]) / 3
		#intensity = each[0] + each[1] + each[2]
		
		# this is another way of choosing the color for the filter
		'''if intensity > 546:
			each = yellow
		elif intensity > 364:
			each = lightBlue
		elif intensity > 182:
			each = red
		else:
			each = darkBlue'''
		if gray_value > 180:
			each = yellow
		elif gray_value > 120:
			each = lightBlue
		elif gray_value > 60:
			each = red
		else:
			each = darkBlue
		new_colors.append(each)
	#image = Image.new("RBG", image.size)
	image.putdata(new_colors)

# make a black and white picture
# Param: Image image
# Return: none
def gray_scale(image):
	new_colors = []
	pixels = list(image.getdata())
	for each in pixels:
		gray_value = (each[0] + each[1] + each[2]) // 3
		pixel_value = (gray_value, gray_value, gray_value)
		each = pixel_value
		new_colors.append(each)
	image.putdata(new_colors)

# invert colors on image
# Param: Image image
# Return: none
def invert_colors(image):
	max_color = 255
	new_colors = []
	pixels = list(image.getdata())
	for each in pixels:
		invert = (max_color - each[0], max_color - each[1], max_color - each[2])
		each = invert
		new_colors.append(each)
	image.putdata(new_colors)
	
# add or subtract a color in the image
# Param: Image image, str color, int color_val
# Return: none
def color_tint(image, color, color_val):
	new_colors = []
	pixels = list(image.getdata())
	#tint each pixel
	for each in pixels:
		if (color == "red"):
			pixel_color = (each[0] + color_val, each[1], each[2])
		elif (color == "green"):
			pixel_color = (each[0], each[1] + color_val, each[2])
		elif (color == "blue"):
			pixel_color = (each[0], each[1], each[2] + color_val)
		each = pixel_color
		new_colors.append(each)
	#this was if the user inputted a tuple instead of a string
	#was unsure about how to go about converting a string into a tuple
	# for each in pixels:
	# 	pixel_color = (each[0] + color_val * color[0], each[1] + color_val * color[1], each[2] + color_val * color[2])
	image.putdata(new_colors)
	
# lowers quality of photo
# Param: Image image, int pixel_size
# Return: none
def pixelate(image, pixel_size):
	# makes sure the pixel_size is valid
	# "valid" means it is a common factor of the image's width and height
	# or else there will be an out of bounds error and no one likes those
	if (image.height % pixel_size != 0 or image.width % pixel_size != 0):
		valid_num = []
		max_val = 0
		if (image.height > image.width):
			max_val = image.height
		else:
			max_val = image.width

		for i in range(1, int(sqrt(max_val))):
			if (image.height % i == 0 and image.width % i == 0):
				valid_num.append(str(i))

		print("Invalid number.")
		print("Try these numbers:")
		print("\n".join(valid_num))
		raise InvalidNum

	# now we'll actually get to work with the image

	# each row chunk starts at size of pixelation * width
	new_row = pixel_size * image.width

	pixels = list(image.getdata())
	new_colors = [0] * len(pixels)

	# iterate through the row and column chunks (defined by how big the pixel_size is)
	# set the pixel color equal to the pixel on the top left of each chunk
	for row in range(0, len(pixels), new_row):
		for column in range(0, image.width, pixel_size):
			for sub_pixel_row in range(pixel_size):
				for sub_pixel_width in range(pixel_size):
					new_colors[row + column + sub_pixel_row * image.width + sub_pixel_width] = pixels[row + column]
	image.putdata(new_colors)


# this was originally the pixelate function, but it ended up resizing the picture instead
# since this function already exists, i've commented it out here
# def resize(image):
# 	# new_height = image.height // 3
# 	# new_width = image.width // 3
# 	pixel_size = 2

# 	new_row = pixel_size * image.width
# 	new_colors = []
# 	new_image = Image.new('RGB',(ceil(image.width / pixel_size), ceil(image.height / pixel_size)), "white")
# 	pixels = list(image.getdata())
# 	for i in range(0, len(pixels), new_row):
# 		for j in range(0, image.width, pixel_size):
# 			new_colors.append(pixels[j])
# 	new_image.putdata(new_colors)
# 	return new_image
