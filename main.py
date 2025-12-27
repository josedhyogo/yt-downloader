#!/usr/bin/env python3
import os,sys,re,subprocess
from downloader import baixarAudio,baixarVideo,respostaDownload,contar_midias
from escolher_pasta_destiono import pastaDestino

# ---------------- VERIFICAÇÃO ----------------
def main():
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


    # ---------------- MENU ----------------
    print("\033[1;31m---------------YT DOWNLOADER---------------\033[m")
    url = input("\033[0;33mDigite a URL da musica/playlist: ").strip()

    opcao = str(input("""Escolha sua opcao:\033[m
    \033[1;36m[ 1 ] - Baixar Video (MP4)
    [ 2 ] - Baixar Áudio (MP3)\033[m
    \033[0;33mDigite aqui:\033[m """)).strip()
    
    total = contar_midias(url)
    print("Total de músicas/videos encontrados: ",total)
    pasta = pastaDestino()
    
    match opcao:
        case "1":
            processo = baixarVideo(url)
            respostaDownload(processo,pasta)
        case "2":
            processo = baixarAudio(url,pasta)
            respostaDownload(processo)
        case _:
            raise ValueError("Opção invalida.(Escolha 1 ou 2).")

if __name__ == "__main__":
    main()