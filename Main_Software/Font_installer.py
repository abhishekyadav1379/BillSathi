import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

class FontInstaller:
    def __init__(self):
        pass

    def is_font_installed(self, font_name):
        # Get a list of installed fonts
        installed_fonts = [f.name for f in fm.fontManager.ttflist]
        
        # Check if the given font is installed
        return font_name in installed_fonts

    def install_font_from_file(self, font_path):
        # Validate the font file path
        if not os.path.exists(font_path):
            print(f"Error: The font file '{font_path}' does not exist.")
            return
        
        # Check if the font is already installed
        font_properties = fm.FontProperties(fname=font_path)
        if self.is_font_installed(font_properties.get_name()):
            print(f"Font '{font_properties.get_name()}' is already installed.")
        else:
            # Install the font
            fm.fontManager.ttflist.append(font_properties)
            plt.rcParams["font.family"] = font_properties.get_name()
            plt.rcParams["font.sans-serif"] = font_properties.get_name()
            print(f"Font '{font_properties.get_name()}' installed successfully.")

if __name__ == "__main__":
    # desired_font = "calibri Bold"
    font_file_path = "./Main_Software/RussoOne-Regular.ttf"  # Replace this with the actual path to your TTF font file

    font_installer = FontInstaller()
    font_installer.install_font_from_file(font_file_path)
