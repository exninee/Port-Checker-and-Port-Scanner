import socket # siteye bağlanmamız için "socket" modülünü çağırıyoruz
print("""


  _______  ___   _ ___ _   _ _____ 
 | ____\ \/ / \ | |_ _| \ | | ____|
 |  _|  \  /|  \| || ||  \| |  _|  
 | |___ /  \| |\  || || |\  | |___ 
 |_____/_/\_\_| \_|___|_| \_|_____|


""")
print("""
(1) Port Checker
(2) Port Scanner 
(3) Exit
""")                                                   #"socket.SOCK_STREAM" ise sunucu ile TCP biçiminde iletişime geçer.
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM) # "socket.AF_INE" komutu ip adresi bilgilerini alıp wep sitesine bağlanıp bilgi alışverişi yapar.
option = int(input("Option >> "))                      
if option == 3 : 
    print("exit...")
    exit

elif option == 1 : 
    target = input("Target Wepsite / Ip >> ")
    port = int(input("Port >> "))
    try:
        s.connect((target , port)) # target ve port değerlerine bağlanıp kontrol etsin.
        print("Port open >> {}".format(port))
    except:
        print("Port Close >> {}".format(port))

elif option == 2 : 
    target = input("Target Wepsite / Ip >> ")
    Min = int(input("Minimum Port >> ")) 
    Max = int(input("Maximum Port >> "))

    for Port in range(Min , Max + 1) : # range fonksiyonu ile girilecek portların kendisi ve aralarındaki sayıları aratmasını sağladık.
        try:
            s.connect((target , Port)) # min ve max değerler ve arasındaki sayılara bağlanıp kontrol etsin.
            print("Port Open >> {}".format(Port))
            break # herşey yolunda ise döngüyü bitirsin.
        except:    
            print("Port Close >> {}".format(Port))

else : 
    print("error :(")
    exit    
