import qrcode

def generate_qr(text, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code generated and saved as {filename}")

if __name__ == "__main__":
    # Prompt the user for the text to encode
    text = input("Enter the text or URL to encode into the QR code: ")
    # Prompt the user for the filename to save the QR code image
    filename = input("Enter the filename to save the QR code image (e.g:my_qr.png): ")
    
    # Generate the QR code
    generate_qr(text, filename)





