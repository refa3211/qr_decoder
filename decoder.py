import cv2
from pyzbar.pyzbar import decode
import flet as ft
import subprocess


def read_qr_code(image_path):
    # Read image using OpenCV
    img = cv2.imread(image_path)
    # Decode QR code
    decoded_objects = decode(img)
    # Print the data from the QR code (assuming it contains a URL)
    for obj in decoded_objects:
        if obj.type == 'QRCODE':
            print('QR Code Data:', obj.data.decode('utf-8'))


def main(page: ft.Page):
    page.theme_mode = page.theme_mode.LIGHT
    page.window_width = 400
    page.window_height = 700
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()

    new_task = ft.TextField(hint_text="What's needs to be done?")

    page.add(new_task, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked))


# if __name__ == '__main__':
#     # image_path = 'test.png'  # Replace with your image file path
#     # read_qr_code(image_path)
#     # ft.app(target=main)

try:
    retcode = subprocess.call("open " + filename, shell=True)
    if retcode < 0:
        print >>sys.stderr, "Child was terminated by signal", -retcode
    else:
        print >>sys.stderr, "Child returned", retcode
except OSError, e:
    print >>sys.stderr, "Execution failed:", e
