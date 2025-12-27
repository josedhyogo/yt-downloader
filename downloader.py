import os,sys,re,subprocess
from escolher_pasta_destiono import pastaDestino
# ---------------- DOWNLOAD ----------------


def respostaDownload(processo):
    for linha in processo.stdout:
        match = re.search(r'(\d+\.\d+%)', linha)
        if match:
            print("Progresso:", match.group(1), end="\r")

    processo.wait()
    print()  # quebra de linha
    if processo.returncode == 0:
        print("\033[1;32mDownload concluído.\033[m")
    else:
        print("\033[1;31mErro no download.\033[m")


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
        text=True,
        cwd=pastaDestino()
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
        text=True,
        cwd=pastaDestino()
    )