import os
import json
from time import sleep
from pytube import YouTube, Search
from pytube import exceptions as pyexc

class color:
    reset = '\033[0m' 
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

def main():
    os.system('')
    user_input = str(input(f'{color.cyan}Insira o nome da música ou o link do Youtube para baixar em formato de música.\n>>> {color.yellow}')).strip()
    if user_input.startswith(("http://", "https://")):
        downloader(method='link', link=user_input)
    elif user_input == '':
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
    else:
        downloader(method='search', link=user_input)

def downloader(method: str, link: str):
    if method == 'search':
        search_msc = Search(link)
        link = search_msc.results[0].watch_url
    try:
        print(f'')
        yt = YouTube(url=link)
        video = yt.streams.filter(only_audio=True).first()
        oldfile = video.download(output_path='musicas/')
        base = os.path.splitext(oldfile)
        newfile = base[0] + '.mp3'
        os.rename(oldfile, newfile)
        print(f'{color.lightgreen}Sucesso! A música: "{video.title}" foi baixada com sucesso!{color.reset}\n\n\n')
    except pyexc.RegexMatchError:
        print(f'{color.red}ERRO! O link inserido não é um link do Youtube. Verifique se inseriu o link corretamente.{color.reset}\n\n')
        sleep(1)
    except pyexc.VideoPrivate:
        print(f'{color.red}ERRO! Este vídeo está privado. Insira um novo link.{color.reset}\n\n')
        sleep(1)
    except (pyexc.AgeRestrictedError, pyexc.VideoRegionBlocked):
        print(f'{color.red}ERRO! Este vídeo está indisponível. Insira um novo link.{color.reset}\n\n')
        sleep(1)
    except pyexc.LiveStreamError:
        print(f'{color.red}ERRO! Este vídeo é uma LiveStream, e não pode ser baixada. Insira o link de um vídeo.{color.reset}\n\n')
        sleep(1)
    except FileExistsError:
        os.remove(oldfile)
        print(f'{color.red}ERRO! Este vídeo já está baixado. Verifique-o na pasta músicas.{color.reset}\n\n')
        sleep(1)
    finally:
        main()

if __name__ == '__main__':
    main()
