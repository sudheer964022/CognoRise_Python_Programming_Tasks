import cv2

def decode_qr(filename):
    img = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = detector.detectAndDecode(img)
    if vertices_array is not None:
        print(f"QR Code detected and decoded text: {data}")
        return data
    else:
        print("No QR Code found")
        return None

if __name__ == "__main__":
    filename = input("Enter the path to the QR code image file: ")
    decoded_text = decode_qr(filename)


