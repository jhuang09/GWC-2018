import filters


TINT = "Color Tint"
OBAMICON = "Obamicon"
GRAY = "Grayscale"
INVERT = "Invert"
PIXELATE = "Pixelate"

filter_options = [
	TINT,
	OBAMICON,
	GRAY,
	INVERT,
	PIXELATE
]

BLUE = "blue"
GREEN = "green"
RED = "red"

# change the name of the file to suit your needs
IMAGE_NAME = "linda.jpg"

def check_num(num):
	while True:
		try:
			num = abs(int(num))
			break
		except ValueError:
			print("Please enter a number.")
			num = input()
	return num

def main():
	print("What kind of filter would you like to apply?")
	print("Here are your options:")
	print("\n".join(filter_options))
	answer = input()
	
	img = filters.load_img(IMAGE_NAME)
	while (answer.lower() != TINT.lower() and answer.lower() != OBAMICON.lower() and
		   answer.lower() != GRAY.lower() and answer.lower() != INVERT.lower() and
		   answer.lower() != PIXELATE.lower()):
		print("Invalid input! Please try again.")
		answer = input()
	
	if (answer.lower() == TINT.lower()):
		color = input("What color would you like tinted? Red, Green, or Blue\n")
		while (color.lower() != BLUE and color.lower() != GREEN and color.lower() != RED):
			print("Invalid input! Please try again.")
			color = input()
		
		value = input("How much do you want it added or subtracted? (Use positive numbers for add and negative for subtract\n")
		# exception handling
		value = check_num(value)
		
		filters.color_tint(img, color, value)
	
	elif (answer.lower() == OBAMICON.lower()):
		filters.obamicon(img)
	
	elif (answer.lower() == GRAY.lower()):
		filters.gray_scale(img)
	
	elif (answer.lower() == INVERT.lower()):
		filters.invert_colors(img)
	
	elif (answer.lower() == PIXELATE.lower()):
		print("How much do you want to pixelate it by? Higher number means more pixelized.")
		print("If you enter a negative number, it'll take the absolute value of it.")
		pixelized_value = input()
		pixelized_value = check_num(pixelized_value)
		while True:
			try:
				filters.pixelate(img, pixelized_value)
				break
			except filters.InvalidNum:
				pixelized_value = input("Try again!\n")
				pixelized_value = check_num(pixelized_value)
	
	filters.save_img(img, "new")


# makes sure that main() is run if I run code from this file
if __name__ == "__main__":
    main()
