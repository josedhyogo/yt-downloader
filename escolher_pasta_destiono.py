import os,sys,re,subprocess

def pastaDestino():
    respostaCriarPs = input("\033[0;33mCriar nova pasta?(s/n):\033[m ").strip().lower()
    
    if respostaCriarPs == 'n':
        return None
    if respostaCriarPs != 's':
        raise ValueError("\033[1;31mValor invalido(Use s ou n).\033[m")

    while True: 
        nome_pasta = input("\033[1;33mNome da pasta: \033[m").strip()
        if not os.path.exists(nome_pasta):
            os.makedirs(nome_pasta,exist_ok=True)
            print('\033[1;32mPasta Criada\033[m')
            return nome_pasta
        else:
            print("\033[1;31mPasta existente. Tente novamente\033[m")
