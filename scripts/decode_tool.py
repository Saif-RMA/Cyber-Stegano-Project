from PIL import Image

def decode_message(image_path):
    # Open the image with error handling
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"[-] Error: file '{image_path}' not found.")
        return

    pixels = list(img.getdata())
    binary_message = ""

    # Extract the LSB (Least Significant Bit) from each RGB channel
    for pixel in pixels:
        for value in pixel[:3]:  # Red, Green, Blue
            binary_message += str(value & 1)

    # Convert groups of 8 bits back into ASCII characters
    all_bytes = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]

    decoded_text = ""
    for byte in all_bytes:
        char = chr(int(byte, 2))
        if char == "\x00":  # Standard end marker
            break
        decoded_text += char

    print(f"\n[+] Secret Message Extracted: {decoded_text}")

if __name__ == "__main__":
    decode_message("../images/hidden_mozarella.png")
