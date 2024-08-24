import os
import platform

# Pull the latest updates from the git repository
os.system('git pull')

# Clear the terminal screen
os.system("clear")

# Print the join WhatsApp group message
print('\033[92;1m Join Whatsapp Group')

# Open the WhatsApp group link
os.system('xdg-open https://chat.whatsapp.com/LDKdovG09Ob2Ai0prMXtCG')

# Detect the system architecture (32-bit or 64-bit)
fbd = platform.architecture()[0]

# Import the "create3" module for both 32-bit and 64-bit systems
if fbd == "32bit" or fbd == "64bit":
    __import__("create3")
else:
    print("Unsupported architecture")
