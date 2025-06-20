import os
import socket
from zipfile import ZipFile

def executar():
    # Executar os arquivadores (garantir que os .exe estão no lugar certo)
    os.system('env\\help_dir.exe') 
    os.system('env\\help_arq.exe')
        
def zipar():
    # Zipar o .txt e o .tar
    with ZipFile("Enviar.zip", "w") as file:
        if os.path.exists('help_dir.txt'): file.write('help_dir.txt')
        if os.path.exists('help_arq.tar'): file.write('help_arq.tar')

def remover():
    # Remover apps ja utilizados especificando o caminho correto
    if os.path.exists('help_dir.txt'): os.remove('help_dir.txt')
    if os.path.exists('help_arq.tar'): os.remove('help_arq.tar')

def enviar():
    from time import sleep
    # Enviar o .zip para o ip 192.168.1.44
    host = '192.168.1.44'
    port = 4443
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            
            with open("Enviar.zip", "rb") as f:
                while True:
                    bytes_read = f.read(4096) # Ler o arquivo em pedaços de 4KB
                    if not bytes_read:
                        break
                    s.sendall(bytes_read)
    except ConnectionRefusedError:
        print("ERRO: A conexão foi recusada. O script de recebimento está rodando no outro computador?")
    except FileNotFoundError:
        print("ERRO: Arquivo Enviar.zip não encontrado. A função zipar() foi executada corretamente?")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    sleep(1.5)
    # os.remove('Enviar.zip')

executar()
zipar()
remover()
enviar()
