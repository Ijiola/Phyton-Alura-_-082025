import os

print('''
      
      𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤 
      
      ''')

print('1.Cadastrar restaurante')
print('2.Listar restaurantes')
print('3.Ativar restaurante')
print('4.Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))
# opcao_escolhida = int(opcap_escolhida)

def finalizar_app():
    os.system('cls')
    # os.system('clear') no mac
    print('Finalizando o app\n')

if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurantes')    
elif opcao_escolhida == 3:
    print('Ativar restaurante') 
else:
    finalizar_app()


