import os,platform
os.system('git pull')
os.system("clear")
print('\033[92;1m [\033[97;1m+\033[92;1m] Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/LDKdovG09Ob2Ai0prMXtCG')
hunter=platform.architecture()[0]
if hunter=="32bit":
    __import__("own3")
elif hunter=="64bit":
    __import__("own3")
