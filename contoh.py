import os
import sys
import time


os.system('clear')
time.sleep(1)
os.system('figlet Hack FB')
print "============================"
print "Author : Rafli"
print "Youtube: Rafli gc"
print "Github : https://github.com/report-set"
print "============================"
print
time.sleep(1)
print "[+] menu pilhan [+]"
print
print "[1] Dark Fbv1.7"
print "[2] Dark Fbv1.8"
print "[3] Dark Fb Premium"
print "[4] Dark Fbv2.0"
print "[5] Install Bahan"
time.sleep(1)
pilih = raw_input('[?] Pilih : ')
if pilih  == "1":
        os.system('git clone https://github.com/report-set/Darkv1.7')
        time.sleep(1)
        print "[+] Penginstallan Selesai"
        time.sleep(1)
        print "[+] Selanjutnya ketik $ cd Darkv1.7"
        time.sleep(1)
        print "[+] Lalu ketik python2 darkfbv1.0.py"
elif pilih == "2":
        os.system('git clone https://github.com/report-set/DarkFbv1.8')
        time.sleep(1)
        print "[+] Penginstallan Selesai"
        time.sleep(1)
        print "[+] Selanjutnya ketik $ cd DarkFbv1.8"
        time.sleep(1)
        print "[+] Lalu ketik python2 DarkFbv1.8.py"
elif pilih == "3":
        os.system('git clone https://github.com/report-set/DarkPremium')
        time.sleep(1)
        print "[+] Penginstallan Selesai"
        time.sleep(1)
        print "[+] Selanjutnya ketik $ cd DarkPremium"
        time.sleep(1)
        print "[+] Lalu ketik python2 darkpremium.py"
elif pilih =="4":
        os.system('git clone https://github.com/report-set/dark-fbv2.0')
        time.sleep(1)
        print "[+] Penginstallan Selesai"
        time.sleep(1)
        print "[+] Selanjutnya ketik $ cd dark-fbv2.0"
        time.sleep(1)
        print "[+] Lalu ketik python2 darkfbv2.0.py"
elif pilih =="5":
        os.system('pkg update && pkg upgrade')
        os.system('pkg install python2')
        os.system('pkg install nano')
        os.system('pkg install git')
        os.system('pip2 install requests mechanize')
        time.sleep(1)
        print "[+] Penginstallan Selesai"

