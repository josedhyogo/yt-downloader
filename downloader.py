import os,sys,re,subprocess
# ---------------- DOWNLOAD ----------------
def contar_midias(url):
    processo = subprocess.run(
        [
            sys.executable, "-m", "yt_dlp",
            "--flat-playlist",
            "--print", "id",
            url
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if processo.returncode != 0:
        print("\033[1;31mErro ao contar mídias:\033[m")
        print(processo.stderr)
        return 0

    linhas = processo.stdout.strip().splitlines()
    return len(linhas)


def respostaDownload(processo):
    atual = None
    total = None

    for linha in processo.stdout:
        # Captura "Downloading item X of Y"
        match_item = re.search(r'Downloading (?:item|video)\s+(\d+)\s+of\s+(\d+)', linha)
        if match_item:
            atual = match_item.group(1)
            total = match_item.group(2)

        # Captura porcentagem
        match_pct = re.search(r'(\d+\.\d+%)', linha)
        if match_pct:
            if atual and total:
                print(f"Progresso: {match_pct.group(1)} ({atual}/{total})", end="\r")
            else:
                print(f"Progresso: {match_pct.group(1)}", end="\r")

    processo.wait()
    print()  # quebra de linha

    if processo.returncode == 0:
        print("\033[1;32mDownload concluído.\033[m")
    else:
        print("\033[1;31mErro no download.\033[m")

def baixarAudio(url,pasta):
    cwd = pasta if pasta else os.getcwd()

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
        cwd=cwd
    )


def baixarVideo(url,pasta):
    cwd = pasta if pasta else os.getcwd()
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
        cwd=cwd
    )