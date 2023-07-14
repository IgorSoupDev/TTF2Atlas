# Usage guide
This tool allows you to generate an atlas containing ASCII characters using a specified font. You can customize various parameters to control the appearance of the generated images. Here's a breakdown of what you can modify:

## Constants
The following constants can be adjusted in the beginning of the code:

- **FONT_PATH**: Specifies the path to the font file (e.g, `example/arial.ttf`).
- **IMAGE_WIDTH**: Sets the width of the generated image (default is 128 pixels).
- **IMAGE_HEIGHT**: Sets the height of the generated image (default is 128 pixels).
- **FONT_SIZE**: Controls the font size in pixels (default is 12).
- **ANTIALIASING**: Determines whether to enable antialiasing (default is False).

## Usage
To use this tool, follow these steps:

- Modify the constants mentioned above to fit your desired settings.
- Make sure you have the required font file (`arial.ttf` in this example) located at the specified path (`example/arial.ttf`).
- Run the code to generate the image file and header file.
- After running the code, it will generate two files:

### Image file 
A PNG image file (`your_font.png`), will be created, containing all the ASCII characters rendered using the specified font and settings.

### Header file
A C header file (`your_font.h`) will be generated, which contains an array of structures. Each structure represents a character and includes information such as the source rectangle (`src`) and position (`posx and posy`) of the character itself. The name of the struct will be `your_font` + `_font`.

**WARNING**: The `src` field of the character uses a data type called RECT that contains the members `x`, `y`, `width`, and `height`. If you don't have this type, you can replace it with something similar or manually add the fields `x`, `y`, `width`, and `height` in the code. I recommend using the `int16_t` type to avoid issues with negative numbers.

## Customization
Feel free to customize the code further to meet your specific requirements. For example, you can modify the range of ASCII characters to include only a subset of characters or add additional functionality.

## License
This tool is released under the MIT License. For more details, please refer to the LICENSE file.
