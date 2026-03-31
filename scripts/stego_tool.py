from PIL import Image

def text_to_bin(text):
    return ''.join(format(ord(i), '08b') for i in text)
    
def hide_message(image_path, secret_text, output_path):
    img = Image.open(image_path)
    binary_secret = text_to_bin(secret_text) + '1111111111111110'
    
    pixels = list(img.getdata())
    new_pixels = []
    data_index = 0 
    
    for pixel in pixels: 
        pixel = list(pixel)
        for i in range(3):
            if data_index < len(binary_secret):
                pixel[i] = (pixel[i] & ~1) | int(binary_secret[data_index])
                data_index += 1 
        new_pixels.append(tuple(pixel)) 
        
    img.putdata(new_pixels)
    img.save(output_path, "PNG")
    print(f"Success! Message hidden in: {output_path}")
    
if __name__ == "__main__": 
   
   hide_message("../images/mozarella.jpg", "You Found the hidden Message! My First Cyber-Project.", "../images/hidden_mozarella.png") 
