import os
import qrcode

output_folder = "qr_codes"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

user_input = input("Enter your link to create a QR code: ")

existing_files = os.listdir(output_folder)

existing_numbers = [
    int(filename.split("_")[1].split(".")[0]) for filename in existing_files if filename.startswith("QrCode_")
]

if existing_numbers:
    file_number = max(existing_numbers) + 1
else:
    file_number = 1

filename = f"QrCode_{file_number}.png"

qr = qrcode.make(user_input)

output_path = os.path.join(output_folder, filename)

qr.save(output_path)

print(f"QR-код для введенной ссылки сохранен в '{output_path}'")
