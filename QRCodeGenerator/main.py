import qrcode

def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    github_url = "https://github.com/Kavya-vinod"
    filename = "github_qr_code.png"
    generate_qr_code(github_url, filename)
    print(f"QR Code for GitHub profile generated and saved as {filename}")
