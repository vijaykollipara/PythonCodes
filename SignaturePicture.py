from PIL import Image
import numpy as np

def convert_to_black_and_white_with_transparency(image_path, output_path):
    try:
        # Open the image
        with Image.open(image_path) as img:
            # Convert the image to grayscale
            bw_img = img.convert('L')
            # Convert grayscale image to RGBA
            rgba_img = bw_img.convert('RGBA')
            img_array = np.array(rgba_img)
            height, width, channels = img_array.shape
            print(f"Image size (height x width x channels): {height} x {width} x {channels}")
            h = 0;
            while(h < height):
                w = 0;
                while(w < width):
                    if((img_array[h,w,0] == 255) and (img_array[h,w,1] == 255) and (img_array[h,w,2] == 255)):
                        img_array[h,w,3] = 0
                    w += 1
                h += 1
            img = Image.fromarray(img_array)
            img.save(output_path, format='PNG')
            print(f"Image saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

input_image_path = "./Sandeep.jpeg"
output_image_path = "./SandeepSignM.png"
convert_to_black_and_white_with_transparency(input_image_path, output_image_path)
