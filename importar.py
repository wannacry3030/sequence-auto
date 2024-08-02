import pymiere
import os

# Diretório onde os arquivos de vídeo estão armazenados
pasta_de_videos = "C:/Users/theel/Videos/teste"

# Lista dos nomes dos arquivos na ordem desejada
# Lista dos nomes dos arquivos na ordem desejada
ordem_dos_arquivos = [
    "27KF4 RICH-POOR KID LUNCH",
    "27KF12 RICH-POOR KID WAKING UP",
    "27KF1 CHANGING CLOTHES",
    "27KF7 RICH-POOR KID BROKEN PHONE",
    "27KF9 RICH-POOR KID JEWELRY",
    "27KF3 FAKE PLANE PICTURE",
    "27KF11 POOR AND RICH KID EATING",
    "27KF14 RICH-POOR KID MORNING ROUTINE",
    "27KF18 RICH KID SPA",
    "27KF5 RICH-POOR KID GIFTS",
    "27KF16 RICH-POOR KID BROKEN CUP",
    "308V2 LOCKERS",
    "308V4 BIRTHDAY AND PRESENTS",
    "308V8 GAMING SITUATION",
    "308V5 CANTEEN",
    "308V7 SPORT",
    "308V3 DRAW",
    "308V1 GUY'S ATTENTION",
    "308V9 BULLYING SITUATION",
    "308V10 SCHOOL PRESIDENT",
    "308V6 PARTY",
    "360F2 ROLY POLY TOY VS DIY FROM BALLOON AND A MARBLE #16820",
    "360F7 POP TUBE DOG VS DIY PAPER DOG #16837",
    "360F5 FINGER SPINNERS VS DIY SPINNERS FROM HOT GLUE #16835",
    "360F6 PREGNANT BARBIE VS DIY #16836",
    "360F3 SQUEEZE BALL VS DIY FROM BALLOON #16833",
    "360F1 POP OUT DINOSAUR EGG VS DIY TOY #16819",
    "360F4 PINEAPPLE POP IT VS DIY HUGE CARDBOARD PINEAPPLE POP IT #16834"
]

# Conectar ao Adobe Premiere Pro
projeto = pymiere.objects.app.project

# Cria uma nova bin (pasta) no painel de projeto
bin = projeto.rootItem.createBin("Bin de Importação")

# Função para importar arquivos e organizá-los na ordem desejada
def importar_arquivos(ordem):
    imported_clips = []
    for arquivo in ordem:
        caminho_arquivo = os.path.join(pasta_de_videos, arquivo + ".mp4")  # Ajuste a extensão conforme necessário
        if os.path.exists(caminho_arquivo):
            projeto.importFiles([caminho_arquivo], False, bin, False)
            imported_clips.append(caminho_arquivo)
        else:
            print(f"Arquivo não encontrado: {caminho_arquivo}")
    return imported_clips

# Chama a função de importação
imported_clips = importar_arquivos(ordem_dos_arquivos)

print("Importação concluída com sucesso!")