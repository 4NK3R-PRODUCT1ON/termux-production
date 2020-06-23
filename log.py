#BY ANKER PRODUCTION
#recode mati lu+corona


from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           os.system("figlet -f slant '   wellcome' | lolcat")
           print('\033[1;96m ============================================================')
           print(' ||  +--------------------------------------------------+  ||')
           print(' ||  | Creator   : ANKER PRODUCTION                             |  ||')
           print(' ||  +--------------------------------------------------+  ||')
           print(' ||  | Youtube   : https://www.youtube/ANKER PRODUCTION    |  ||')
           print(' ||  | github    : https://github.com/4NK3R-PRODUCT1ON/termux-production       |  ||')
           print(' ||  | WhatsApp  : +1 (234) 985-0607                         |  ||')
           print(' ||  | Team      : L.A.S.S                       |  ||')
           print(' ||  +--------------------------------------------------+  ||')
           print(' ============================================================')
           print("")
           try:
                x = str(input('\033[1;92m [?] Username \033[1;93m: '))
                print("")
                e = getpass('\033[1;92m [?] Password \033[1;93m: ')
                print ("")
#silahkan ganti username+passwordnya gan
                if x=="BTWSUBS" and e=="ANKERLBK":
#jangan edit yg lain kalo gak mau eror
                   print('Login Sukses Mohon Tunggu Sebentar...')
                   time.sleep(1)
                   os.system('clear')
                   print('')
                   os.system('figlet ' + x + ' | lolcat')
                   print('\033[1;92m ────────────────────────────────|by Moreno77 ')
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     [!] Username/Password Salah")
                      time.sleep(2)
                      print("")
           except Exception:
                      
                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     [!] Username/Password Salah")
                      time.sleep(2)
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     [!] Username/Password Salah")
                      time.sleep(2)
menu()
