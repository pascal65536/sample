from PIL import Image

if __name__ == "__main__":
    inputfile = "lighter.webp"
    outfile = "outfile.jpg"
    size = (1024, 512)
    with Image.open(inputfile) as im:
        print(im.format, im.size, im.mode)
        im.thumbnail(size)
        im.save(outfile, "JPEG")
