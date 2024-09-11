import os
import platform

os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[92;1m [\033[97;1m•\033[92;1m] Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/DsCVNjYtO5027qagbKaNbJ')

saqi = platform.architecture()[0]

if saqi == "32bit":
    os.system("clear")
    exit("\033[91;1m 32Bit Device Not Supported")

elif saqi == "64bit":
    try:
        __import__("cook2")
    except ImportError as e:
        print(f"\033[91;1m ImportError: {e}")
        print("\033[91;1m Ensure that 'cook2' is compiled for 64-bit architecture.")
