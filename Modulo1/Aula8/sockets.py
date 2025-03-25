"""
Sockets - São pontos de comunicação que permitem a troca de informações entre
processos. Podem ser usados para comunicar entre processos na mesma máquina ou 
entre máquinas diferentes. 

O código que escrevemos abaixo mostra como os sockets são importantes
na conexão entre usuário e servidor (nesse caso, pentester e servidor). 
Isso pode ser útil para encontrar portas abertas e possíveis vulnerabilidades.

socket.AF_INET = insicação de que estamos usando IPv4
socket.SOCK_STREAM = indicação de que estamos usando o protocolo TCP
"""

"""
Porta 80(HTTP) -- É usada para tráfego HTTP (HyperText Transfer Protocol), que trasmite
dados sem criptografia. Quando você acessa um site digitando apenas http://..., sua 
requisição passa pela porta 80. Por isso ela está quase sempre aberta. 

Porta 443(HTTPS) -- É usada para tráfego HTTPS (HyperText Transfer Protocol Secure), que
adiciona uma camada de segurança via SSL/TLS. Isso garante que os dados trocados entre 
o cliente e o servidor sejam criptografados, protegendo contra ataques como interceptação
e adulteração. Quando você acessa um site digitando apenas https://..., sua 
requisição passa pela porta 443.

"""
import socket

# Fazendo a conexão com o site 
dominio = input("Digite o Alvo: ")
porta = 80 # Porta padrão para HTTP
conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criação do socket

# Definição de tempo limite para conexão
conexao.settimeout(0.5)

# Tentativa de conexão
scan = conexao.connect_ex((dominio, porta))
if scan == 0:
    print(f"The door {porta} is Open")
else:
    print(f"The door {porta} is Closed")