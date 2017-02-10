#ecoding:utf-8
import socket
print"""
########################
AlienWare Port Scanning
########################
                         |----.___
                                |----.___',
              ._________________|_______________.
              |####|    |####|    |####|   |####|
              |####|    |####|    |####|    |####|       .
              |####|    |####|    |####|    |####|     /|_____.
  __          |####|    |####|    |####|    |####|   |  o  ..|
(  '.         '####|    '####|    '####|    '####|   '.  .vvv'
 '@ |          |####.    |####.    |####.    |####|    ||
  | |          '####.    '####.    '####.    '####.    ||
 /  |         /####.    /####.    /####.    /####.     |'.
|    |       '####/    '####/    '####/    '####/      |  |
|     |  .  /####|____/####|____/####|____/####|      |    |
|      |//   .#'#. .*'*. .#'#. .*'*. .#'#. .*'*.     |      |
 |     //-...#'#'#-*'*'*-#'#'#-*'*'*-#'#'#-*'*'*-...'        |
  |   //     '#'#' '*'*' '#'#' '*'*' '#'#' '*'*'             |
   './/                                                     .'
   _//'._                                                _.'
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
[+] -h para instrucoes [+]
[+] Port Scanning 1.1 [+]
[+] AlienWare [+]
[+] Greetz: Diogo@Makaveli - Op@Coder - Júlia Siilva- Luis Henrique [+]
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

help = raw_input("[+] Digite -h [+] : ")

if help == '-h':
    print"""
        Codado by SadStan
        Greetz: Diogo Makaveli - Júlia Siilva - OpCoder - Luis Henrique
        PortScan 1.1
        AlienWare

        exit [para sair]
        -h [para help]
    """
elif help == 'exit':
    exit()
else:
    print"Opcao invalida"

ip = raw_input("[+] IP OR ADDRESS [+]: ")

if ip == "exit":
    exit()

elif ip == '-h':
    print"""
        Codado by SadStan
        Greetz: Diogo Makaveli - Júlia Siilva - OpCoder - Luis Henrique
        PortScan 1.0
        AlienWare

        exit [para sair]
        -h [para help]
    """
    exit()
else:
    print("[+] Carregando [+]")
    print("\n")
ports = []
count = 0

while count < 10:
    ports.append(int(raw_input("[+] PORT [+]: ")))
    count +=1

if str(ports) == "exit":
    exit()

elif str(ports) == "-h":
    print"""
        Codado by SadStan
        Greetz: Diogo Makaveli - Júlia Siilva - OpCoder - Luis Henrique
        PortScan 1.0
        AlienWare

        exit [para sair]
        -h [para help]
    """
else:
    print("[+] Carregando [+]")

print("\n")
for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.15)
    code = client.connect_ex((ip, port))

    if code == 0:
        print("\n")
        print str("+++++++++++++++++++++++++")
        print str("Porta")
        print str(port) +" [Aberta] "
        print str("+++++++++++++++++++++++++")
    else:
        print("\n")
        print str("+++++++++++++++++++++++++")
        print str("Porta")
        print str(port) +" [Fechada]"
        print str("+++++++++++++++++++++++++")
print("\n")
print("++++++++++++++++++++++++++")
print("O SCAN FOI FINALIZADO")
print("++++++++++++++++++++++++++")
