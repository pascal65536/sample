from PIL import Image


if __name__ == "__main__":
    inputfile = "2.jpg"

    input_im = Image.open(inputfile)
    if input_im.mode != "RGBA":
        input_im = input_im.convert("RGBA")

    # Найдём цвет для градиента
    unique_colors = dict()
    pixel_count = 0
    for i in range(input_im.size[0]):
        for j in range(input_im.size[1]):
            pixel = input_im.getpixel((i, j))
            unique_colors.setdefault(pixel, 0)
            unique_colors[pixel] += 1
            pixel_count += 1
    max_color = (0, 0, 0)
    max_color_count = 0
    for k, v in unique_colors.items():
        if v > max_color_count and len(set(list(k)[0:3])) > 1:
            max_color_count = v
            max_color = k

    unique_colors = dict(sorted(unique_colors.items(), key=lambda item: item[1]))

    for k, v in unique_colors.items():
        # if v > (pixel_count//100 ):
        print(k, v / pixel_count * 100)

    print("\n")
    print(pixel_count)
    print(max_color)
    print(max_color_count)
