# Unlock PDF, Created by Nadeem Shah. Using open source libraries.

# Use at your own risk. I am not responsible for any consequences resulting from its use.

# You will need to install the pikepdf library as a pip install.

# MORE INFORMATION ON THIS LIBRARY CAN BE FOUND HERE:

# https://pypi.org/project/pikepdf/10.9.1/#description

import pikepdf
import os

# Create a temp directory if does not exist.

os.makedirs('temp', exist_ok=True)

pdf = pikepdf.open('yourpdffile.pdf', allow_overwriting_input=True)
pdf.save('temp/unlocked.pdf')
