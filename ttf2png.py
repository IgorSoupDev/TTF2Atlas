"""
MIT License

Copyright (c) 2023 SoupDev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
from PIL import Image, ImageDraw, ImageFont

# Constants
FONT_PATH = "example/arial.ttf"
IMAGE_WIDTH = 128
IMAGE_HEIGHT = 128
FONT_SIZE = 12
ANTIALIASING = False


# Define the range of ASCII characters to convert to images
FIRST_ASCII_CHARACTER = ord(" ")  # Space
LAST_ASCII_CHARACTER = ord("~")

# Remove the file extension from the entire path
PATH_WITHOUT_EXTENSION = os.path.splitext(FONT_PATH)[0]

# Remove the directory path, leaving only the file name
FILE_NAME = os.path.basename(FONT_PATH)

# Load the font and create a new image
font_data = ImageFont.truetype(FONT_PATH, FONT_SIZE)
font_image = Image.new(mode="RGBA", size=(IMAGE_WIDTH, IMAGE_HEIGHT))
font_draw = ImageDraw.Draw(font_image)

current_x = 0
current_y = 0

# Disable anti-aliasing
font_draw.fontmode = "L" if ANTIALIASING else "1"

characters = []
character_positions = []

class RECT:
	def __init__(self):
		self.char = ""
		self.x = 0
		self.y = 0
		self.w = 0
		self.h = 0

class Vector2:
	def __init__(self):
		self.x = 0
		self.y = 0

# Function to calculate character properties
def calculate_character_properties(character, pos):
	# Get bbox left ascender and set character object and its properties
	bbox_left_ascender = font_draw.textbbox((current_x, current_y), character.char, font=font_data, anchor="la")
	character.x, character.y, character.w, character.h = bbox_left_ascender
	character.w -= character.x
	character.h -= character.y

	# Get bbox_left_top
	bbox_left_top = font_draw.textbbox((current_x, current_y), character.char, font=font_data, anchor="lt")
	pos.x = bbox_left_ascender[0] - bbox_left_top[0]
	pos.y = bbox_left_ascender[1] - bbox_left_top[1]

# Draw each ASCII character in the image
for i in range(FIRST_ASCII_CHARACTER, LAST_ASCII_CHARACTER + 1):
	# Create a character object, position and set its properties
	character = RECT()
	character.char = chr(i)
	character_pos = Vector2()

	calculate_character_properties(character, character_pos)

	# Check if current row is full, then move to the next row and upda character properties
	if current_x + character.w >= IMAGE_WIDTH - 1:
		current_x = 0
		current_y += FONT_SIZE
		calculate_character_properties(character, character_pos)

	# Draw the character on the image
	font_draw.text((current_x, current_y), chr(i), font=font_data, anchor="la")

	# Update the current position
	current_x += character.w

	# Append the character and its position to the respective lists
	characters.append(character)
	character_positions.append(character_pos)

# Save the image
font_image.save(PATH_WITHOUT_EXTENSION + ".png")


# Generate the header file
H_STRUCT = f"""static const struct
{{
	RECT src;
	int16_t posx, posy;
}} {os.path.splitext(FILE_NAME)[0]}_font[0x60] = {{
"""

with open(PATH_WITHOUT_EXTENSION + ".h", "w") as file:
	file.write(H_STRUCT)
	for character, position in zip(characters, character_positions):
		# Hardcoding some characters name
		if character.char == " ":
			character.char = "space"
		if character.char == "\\":
			character.char = "backslash"

		# Write the character information to the file
		file.write(f"   {{{{{character.x}, {character.y}, {character.w}, {character.h}}}, {position.x}, {position.y}}}, // {character.char}\n")
	file.write("};")