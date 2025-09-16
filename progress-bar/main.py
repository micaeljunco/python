import os
import time
import math

# Função que desenha a barra de progresso
def progress_bar(perc, still):
    # Aguarda para ter efeito animado
    time.sleep(0.01)
    
    prog_char = "$"
    still_char = "/"

    print(f"({perc}/100%)\t", end='')  # Mostra a porcentagem
    
    # Para diminuir o tamanho da barra de progresso
    perc_blocks = math.floor(perc/1.6)
    still_blocks = math.floor(still/1.6)

    # Exibe a barra de progressio.
    print(f"[\033[36m{prog_char*perc_blocks}\033[0m{still_char*still_blocks}]", end ='\r')
    
    return 0


def file_process(dir):    
    # Cria um array com o nome de todos os arquivos do diretorio
    contents = os.listdir(dir)
    
    # Caso não tenha arquivo algum para exluir, retorna
    if len(contents) == 0:
        return 1

    print(f"Removendo {len(contents)} arquivos encontrados em {dir}\n")
    
    # Inicializa um contador do index do arquivo 
    fi = 0

    # Pra cada arquivo em contents (pasta com arquivos a serem processados), faça
    for file in contents:
        # Soma no index
        fi+=1
        # Obtem a porcentagem de arquivos processados de 0 a 100%
        perc = math.floor(fi/len(contents)*100)     # utiliza-se o floor para obter um valor inteiro
        # Quantos arquivos ainda faltam para serem processados
        still = 100 - perc

        # Chama a função que desenha a barra de progresso na tela
        progress_bar(perc, still)
        
        # Remove os arquivos
        os.remove(os.path.join(dir, file))
        
    print("\nOperções concluídas!")
    
    return 0


def main():
    # __file__ contem o caminho do arquivo atual
    # abspath() retorna o caminho absoluto
    # dirname() remove o nome do arquivo no final do caminho
    basePath = os.path.dirname(os.path.abspath(__file__)) 
    junk_dir = os.path.join(basePath, "junk")

    # exists() testa se um diretório existe
    if not os.path.exists(junk_dir):
        print(f"\n{junk_dir} não encontrado.\n")
        # Retorna um erro
        return 1
    
    if file_process(junk_dir):
        print(f"\nNenhum arquivo foi encontrado em {junk_dir}\n")
        return 1
                
    # Finaliza sem erros
    return 0

main()