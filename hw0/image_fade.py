from PIL import Image

def main():
    input_image = Image.open("westbrook.jpg")
    width,height = input_image.size
    
    for i in range(width):
        for j in range(height):
                r,g,b = input_image.getpixel((i,j))
                r,g,b = r/2,g/2,b/2
                input_image.putpixel((i,j),(r,g,b))
    
    input_image.save("output.jpg")

if __name__ == "__main__":
    main()

