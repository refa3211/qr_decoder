
import flet as ft
from pydantic import FilePath

from pyzbar.pyzbar import decode
from PIL import Image

def decode_qr_code(file_path):
    # Open and load the image file
    img = Image.open(file_path)

    # Decode QR code
    qr_codes = decode(img)

    if qr_codes:
        # Extract and return the decoded data (assuming there's only one QR code in the image)
        return qr_codes[0].data.decode('utf-8')
    else:
        return "No QR code found or could not decode."


def main(page: ft.Page):
    page.theme_mode = 'LIGHT'
    page.window_width = 700
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def on_file_picked(e: ft.FilePickerResultEvent):
        if e.files:
            print(f"e: files: {e.files[0].path}")
            file_path.value = e.files[0].path
            file_path.value = decode_qr_code(e.files[0].path)
            qr_tbox.value = decode_qr_code(e.files[0].path)
        else:
            file_path.value = "No file selected"
        page.update()

    file_picker = ft.FilePicker(on_result=on_file_picked)

    page.overlay.append(file_picker)
    
    qr_tbox = ft.TextField(value="QR: ", width=400, adaptive=True)
    file_path = ft.Text(value="No file selected")
    pick_file_button = ft.ElevatedButton(
        text="Pick a file",
        on_click=lambda _: file_picker.pick_files()
    )

    page.add(pick_file_button, file_path, qr_tbox)
    print(file_path.value)

ft.app(target=main)