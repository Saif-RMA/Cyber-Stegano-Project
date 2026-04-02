from PIL import Image

def decode_message(image_path):
    #1 Open the Hacked Image
    img = Image.open(image_path)
    pixels = list(img.getdata())
    
    binary_message = ""
    
    
    #2 Extract the LSB (Least significant bit) from each RGB value
    for pixel in pixels:
        for value in pixel[:3]: # Loops through Red, Green and Blue
            # The '& 1' operation checks if the number is even (0) or odd (1)
            binary_message += str(value & 1)
            
    #3 Convert groups of 8 bits back into ASCII characters
    all_bytes = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    
    decoded_text = ""
    for byte in all_bytes: 
        #Convert binary string to integer, then integer to character
        decoded_text += chr(int(byte, 2))
            
        # Stop once we see a common endf of sentence or a specific marker
        if "." in decoded_text and len(decoded_text) > 50:
            break
            
    print(f"\n[+] Secret Message Extracted: {decoded_text}")
    
if __name__ == "__main__":
    decode_message("../images/hidden_mozarella.png")
