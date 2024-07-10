import qrcode

def generate_qr_code(input_data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

if __name__ == "__main__":
    data = input("Введите текст или URL для создания QR-кода: ")
    filename = input("Введите имя файла для сохранения QR-кода (например, qr_code.png): ")

    generate_qr_code(data, filename)
    print(f"QR-код успешно сохранен в файле {filename}")