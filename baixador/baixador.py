import subprocess
import re
import sys

# ---------------- VERIFICAÇÃO ----------------

def yt_dlp_instalado():
    try:
        subprocess.run(
            [sys.executable, "-m", "yt_dlp", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True
        )
        return True
    except Exception:
        return False


if not yt_dlp_instalado():
    print("yt-dlp não encontrado. Instalando via pip...")
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--user", "yt-dlp"],
        check=False
    )

    if not yt_dlp_instalado():
        print("Falha ao instalar yt-dlp.")
        sys.exit(1)
else:
    print("yt-dlp pronto para uso.")

# ---------------- DOWNLOAD ----------------

def respostaDownload(processo):
    for linha in processo.stdout:
        match = re.search(r'(\d+\.\d+%|\d+%)', linha)
        if match:
            print("Progresso:", match.group(1), end="\r")

    processo.wait()
    print()  # quebra de linha
    if processo.returncode == 0:
        print("Download concluído.")
    else:
        print("Erro no download.")


def baixarAudio(url):
    return subprocess.Popen(
        [
            sys.executable, "-m", "yt_dlp",
            "-f", "bestaudio",
            "-x", "--audio-format", "mp3",
            url
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )


def baixarVideo(url):
    return subprocess.Popen(
        [
            sys.executable, "-m", "yt_dlp",
            "-f", "bestvideo+bestaudio",
            "--merge-output-format", "mp4",
            url
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

# ---------------- MENU ----------------

url = input("Digite a URL da musica/playlist: ").strip()

opcao = int(input("""Escolha sua opcao:
1 - Baixar Video (MP4)
2 - Baixar Áudio (MP3)
"""))

match opcao:
    case 1:
        processo = baixarVideo(url)
        respostaDownload(processo)
    case 2:
        processo = baixarAudio(url)
        respostaDownload(processo)
    case _:
        print("Opção invalida.")
