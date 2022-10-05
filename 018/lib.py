import random
import colorgram


def random_color():
    """Returns a tuple with the (r, g, b) color."""
    rgb_colors = [
        (249, 248, 248),
        (238, 246, 243),
        (246, 240, 244),
        (235, 241, 246),
        (1, 13, 31),
        (52, 25, 17),
        (219, 127, 106),
        (9, 105, 160),
        (242, 214, 69),
        (150, 84, 39),
        (215, 87, 64),
        (164, 162, 32),
        (158, 6, 24),
        (157, 62, 102),
        (11, 63, 32),
        (97, 6, 19),
        (207, 74, 104),
        (10, 97, 58),
        (0, 63, 145),
        (173, 135, 162),
        (7, 172, 216),
        (158, 34, 24),
        (3, 213, 207),
        (8, 140, 85),
        (145, 227, 216),
        (122, 193, 148),
        (102, 220, 229),
        (221, 178, 216),
        (253, 197, 0),
        (80, 135, 179),
        (122, 169, 190),
        (29, 85, 93),
    ]
    return random.choice(rgb_colors)


def extract_colors(file, amount_of_colors):
    """Takes an image and returns a list of tuples with (r,g,b) values for each extracted color"""
    rgb_colors = []
    colors = colorgram.extract(file, amount_of_colors)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))
    return rgb_colors
