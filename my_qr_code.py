import qrcode
from PIL import Image
from PIL import Image, ImageDraw
import os

data = "https://github.com/Genzcoder69"

file_path = r"C:\Users\hp\OneDrive\Desktop\Python\logo.jpg"
output_file = r"D:\4k Wallpaper\colored_qr_with_logo.png"



qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# This code is for generating coloured QR code 
qr_img = qr.make_image(
    fill_color = "black",
    back_color = "grey"
).convert("RGBA")

logo = Image.open(r"D:\4k Wallpaper\logo.jpg").convert("RGBA")

qr_width, qr_height = qr_img.size
logo_size = qr_width //4

logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# Create circular mask
mask = Image.new("L", (logo_size, logo_size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, logo_size, logo_size), fill=255)

# Apply mask to logo for making it circular
circular_logo = Image.new("RGBA", (logo_size, logo_size))
circular_logo.paste(logo, (0, 0), mask)


# position logo at center
logo_position = (
    (qr_width - logo_size) //2,
    (qr_height - logo_size) //2,
    
)

# Paste logo 
qr_img.paste(circular_logo, logo_position, circular_logo)

# Save final qr code
qr_img.save(output_file)

print("QR generated successful>>>")
print("Saved at: ",output_file)