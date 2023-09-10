import win32print
import win32ui
from PIL import Image, ImageWin

class PrinterManager:
    PHYSICALWIDTH = 110
    PHYSICALHEIGHT = 111

    @staticmethod
    def print_image(printer_name, file_name):
        hDC = win32ui.CreateDC()
        hDC.CreatePrinterDC(printer_name)
        printer_size = hDC.GetDeviceCaps(PrinterManager.PHYSICALWIDTH), hDC.GetDeviceCaps(PrinterManager.PHYSICALHEIGHT)
        # print(printer_size)
        
        bmp = Image.open(file_name)
        # print("image size:", bmp.size[0], bmp.size[1])
        img_width = bmp.size[0]
        img_height = bmp.size[1]

        hDC.StartDoc(file_name)
        hDC.StartPage()

        printer_width = printer_size[0]
        printer_height = int(img_height * (1678 / 10000))  # You can adjust this calculation as needed
        # print(f"printer size: {printer_width}, {printer_height}")

        dib = ImageWin.Dib(bmp)
        dib.draw(hDC.GetHandleOutput(), (0, 0, printer_width, printer_height))

        hDC.EndPage()
        hDC.EndDoc()
        hDC.DeleteDC()

# Usage
# printer_name = "Everycom-80-Series"
# file_name = "image.png"

# PrinterManager.print_image(printer_name, file_name)
