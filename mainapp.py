import os
import shutil

def esvaziar_lixeira(unidade):
    lixeira_path = f"{unidade}:\\$Recycle.Bin"
    
    if os.path.exists(lixeira_path):
        try:
            for root, dirs, files in os.walk(lixeira_path):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir in dirs:
                    shutil.rmtree(os.path.join(root, dir))
            print(f"Lixeira de {unidade}: esvaziada com sucesso.")
        except Exception as e:
            print(f"Erro ao esvaziar a lixeira de {unidade}: {e}")
    else:
        print(f"Lixeira de {unidade}: não encontrada.")

def esvaziar_lixeiras():
    for letra in range(ord('C'), ord('Z') + 1):
        unidade = chr(letra)
        esvaziar_lixeira(unidade)

if __name__ == "__main__":
    esvaziar_lixeiras()
