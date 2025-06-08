# Bibliotecas Importadas
import os

# Tool que verifica o ip da maquina
def my_ip():

    print("---------------------------------------------------------------")
    # Retorna o endereço IPV4
    os.system("ifconfig wlp1s0 | grep 'inet ' | echo  YOUR IPV4 IS: $(awk '{print $2}')")
    # Retorna o endereço IPV6
    os.system("ifconfig wlp1s0 | grep 'inet6 ' | echo YOUR IPV6 IS: $(awk '{print $2}')")
    print("---------------------------------------------------------------\n")

# Tool que verifica o endereço ip de um dominio
def dns_server():

    print("---------------------------------------------------------------")
    # Exemplos
    print('nslookup [DOMAIN]')
    print('nslookup www.example')
    # Input para pegar o dominio do site
    domain = input("nslookup ")
    #parte do codigo para o OS.SYSTEM
    rest_the_code = "grep 'Address: 1' | echo THE IP ADDRESS IS: $(awk '{print $2}')"
    os.system(f"\nnslookup {domain} | {rest_the_code}")
    print("---------------------------------------------------------------\n")

# Tool que faz um teste de conectividade com uma maquina
def ping():

    print("---------------------------------------------------------------")
    # Exemplos
    print("ping [IP or DOMAIN]")
    print("EX: ping 192.168.9.9 or www.example.com\n")
    # Input para pegar o IP
    ip = input("ping ")
    # Envia 5 pacotes para testar conectividade
    os.system(f"ping -c 5 {ip}")
    print("---------------------------------------------------------------\n")


# Tool que verifica a rota de um pacote até uma maquina
def packet_traffic():
    print("---------------------------------------------------------------")
    # Exemplos
    print("traceroute [IP or DOMAIN]")
    print("Ex: traceroute 192.168.1.3 or www.example.com")
    # Input para pegar o IP ou DOMAIN
    ip_domain = input("traceroute ")
    os.system(f"traceroute {ip_domain}")
    print("---------------------------------------------------------------\n")

# Função que junta todas as outras funções
def main():

        # Titulo e meunu de opções
    menu = ("""
███╗░░░███╗██╗░░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
████╗░████║╚██╗░██╔╝  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
██╔████╔██║░╚████╔╝░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
██║╚██╔╝██║░░╚██╔╝░░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
██║░╚═╝░██║░░░██║░░░  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
╚═╝░░░░░╚═╝░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░

[0] CHECK IP.
[1] CHECK DOMAIN DNS.
[2] PING CONNECTIVITY.
[3] TRAFFIC ROUTE.
[4] TO GO OUT. 


: """)
    
    # Dicionario que lista minha Tools
    actions = {
        0: my_ip,
        1: dns_server,
        2: ping,
        3: packet_traffic
    }

    # Loop
    while True:

        try:
            opc = int(input(menu))

            # Opção para encerrar o programa
            if opc == 4:
                os.system("clear")
                print("TOOLS CLOSED")
                break

            elif opc in actions:
                actions[opc]()

            else:
                print("OPTION NOT AVAILABLE")

        except ValueError:
            print("INVALID INPUT. PLEASE ENTER A NUMBER.")

        # Retorna ao menu inicial
        input("PRESS ENTER TO RETURN TO THE MAIN MENU!")
        os.system("clear")
            
# Chama o programa principal
if __name__ == "__main__":
    main()