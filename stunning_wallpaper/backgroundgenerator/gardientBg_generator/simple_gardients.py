from PIL import Image, ImageFilter, ImageDraw


def horizontal_graident(image: Image.Image, color_list) -> Image.Image:
    # N Horizontal Graident
    width, height = image.size
    img_draw = ImageDraw.Draw(image)
    block_width = width//len(color_list)
    for i, c in enumerate(color_list):
        img_draw.rectangle((
            ((block_width) * (i), 0),
            ((block_width) * (i+1), height)
        ), c)

    image = image.filter(ImageFilter.GaussianBlur(block_width))
    return image


def vertical_gradient(image: Image.Image, color_list) -> Image.Image:
    # N Vertical Graident
    width, height = image.size
    img_draw = ImageDraw.Draw(image)
    block_height = height//len(color_list)
    for i, c in enumerate(color_list):
        img_draw.rectangle((
            (0, (block_height) * (i)),
            (width, (block_height) * (i+1))
        ), c)
    image = image.filter(ImageFilter.GaussianBlur(block_height))
    return image
