from pathlib import Path 

def encontra_arquivo(nome_arquivo, caminho=Path.home()):
    """
    A função encontra o Path absoluto do arquivo passado no parâmetro
    Args: 
    nome_arquivo (string) = nome do arquivo sem extensão 
    Caminho(Path): Caminho onde o arquivo se encontra. Default = Path.home()
    """
    for arquivo in caminho.glob('**/*'):
        # Verifica se é um arquivo e retorna um bool
        if arquivo.is_file():
            # .stem retorna o nome do arquivo SEM extensão
            if arquivo.stem == nome_arquivo:
                return arquivo

