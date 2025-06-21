# Bibliotecas Importadas
import os

# Tool que verifica o ip da maquina
def my_ip():

    # Bilioteca Importada
    import socket
    print("---------------------------------------------------------------")
    # "TRY / EXCEPT" para lidar com erros(exceções)
    try:
        # Conecta a um IP público qualquer sem enviar dados (só para descobrir a interface de saída)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80)) # Google DNS
        ip = s.getsockname()[0]
        s.close()
        print(f"YOUR IPV4 IS: {ip}")
    except Exception as e:
        print(f"Erro ao obter IP: {e}")
    print("---------------------------------------------------------------\n")

# Tool que verifica o endereço ip de um dominio
def dns_server():

    # Bilioteca Importada
    import socket
    print("---------------------------------------------------------------")
    # Exemplos
    print('nslookup [DOMAIN]')
    print('nslookup www.example')
    # Input para pegar o dominio do site
    domain = input("nslookup ")
    # "TRY / EXCEPT" para lidar com erros(exceções)
    try:
        ip = socket.gethostbyname(domain)
        print(f"O IP do domínio {domain} é: {ip}")
    except socket.gaierror:
        print("Domínio Inválido.")
    print("---------------------------------------------------------------\n")

# Tool que faz um teste de conectividade com uma maquina
def ping():

    # Bilioteca Importada
    import subprocess
    print("---------------------------------------------------------------")
    # Exemplos
    print("ping [IP or DOMAIN]")
    print("EX: ping 192.168.9.9 or www.example.com\n")
    # Input para pegar o IP
    ip = input("ping ")
    # "TRY / EXCEPT" para lidar com erros(exceções)
    try:
        # Envia 5 pacotes para testar conectividade
        subprocess.run(["ping", "-c", "5", ip], check=True)
    except subprocess.CalledProcessError:
        print("Erro ao executtar o ping.")
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