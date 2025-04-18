"""
Scanner de portas. 
Objetivo = verificar se a porta 445 (ou outras) do google.com está aberta ou fechada, 
utilizando sockets para tentar estabelecer uma conexão com essa porta. 
Se a conexão for bem sucedida, o programa retorna 0 como resultado. Se a conexão falhar
retorna um código de erro diferente de zero.

Porta 445(SMB) -- É usada pelo protocolo SMB (Server Message Block), que permite 
compartilhamento de arquivos, impressoras e outros reursos entre computadores em

"""
import socket 
hostname = "google.com"
porta = [80]

for p in porta: # Itera sobre a lista de portas 
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um socket TCP/IP
    cliente.settimeout(0.5) # Define um tempo limite para a conexão
    scan = cliente.connect_ex((hostname, p)) # Tenta se conectar ao host na porta p
    
    if scan == 0:
        print(f"Porta {p} ABERTA em {hostname}")
    else:
        print(f"Porta {p} FECHADA em {hostname}")

