class Celular:
    #atributos
    marca= None
    modelo = None
    fabricação = None
    memoria_max = None
    memoria_atual = 0
    ram_max = None
    cor = None
    sistema_operacional=None
    estado='desligado'
    app=[]
    
    
    
    
    #métodos
        
    def ligar(self):
        if self.estado == 'ligado':
            print('O celular está ligado')
        else: 
            self.estado = 'ligado'
            print(f'O celular se encontra:{self.estado}')
    
    def desligar(self):
        if self.estado == 'ligado':
            while True:
                pergunta = input("Deseja desligar o celular? ").lower().strip()
                if(pergunta[0] != "n"):
                    
                    break
                self.estado = 'desligado'
                print(f'O celular será:{self.estado}')
        
    def baixar_app(self):
        if self.estado == 'ligado':
            while True:
                resposta = input("Deseja baixar algum app? ").lower().strip()
                if(resposta[0] != "n"):
                    app = input("Digite o nome do app: ")
                    memoria_app = int(input("Digite a memoria do app: "))
                    if memoria_app <= self.memoria_atual:
                        self.app.append(app)
                        self.memoria_atual -= memoria_app
                        print(f'{app} foi instalado, ele ocupa {memoria_app} GB de memória.')
                        print(f'Você possui {self.memoria_atual} GB de memória.')
                    else:
                        print(f'Memoria cheia')   
                else:
                    break
                resposta = input("Deseja adcionar outro app? ").lower().strip()
                if(resposta[0] == "n"):
                    break
        else:
            ('Ligue o celular!')
            
    def excluir_app(self):
        while True:
            if(not self.app):
                print("Você não possui apps no celular")
            else:    
                print("Essa é a lista de aplicativos")
                print(self.app)
            resposta = input("Deseja excluir algum app? ").lower().strip()
            if(resposta[0] == "n"):
                break
            else:
                app = input("Digite o nome do aplicativo que deseja excluir: ")
                memoria_app = int(input("Digite a memoria que o app ocupa no celular: "))
            if self.estado=='ligado':
                    if app in self.app:
                        self.app.remove(app)
                        self.memoria_atual+=memoria_app
                        print(f'Voce removeu o {app} ')   
                        print(f'Essa é sua atual memoria no seu celular {self.memoria_atual}') 
                    else:
                        print(f'Voce nao possui o {app} ')    
        else:
            print('Ligue o celular!')
            

                 
#criação do objeto
   
cell = Celular() 
cell.marca=input('Digite a marca do seu celular!')
cell.modelo=input('Digite o modelo do seu celular!')
cell.fabricação = int(input('Digite o ano de fabricação do seu celular!'))
cell.memoria_max=int(input('Digite o memoria do seu celular!'))
cell.memoria_atual = cell.memoria_max
cell.cor=input('Digite o cor do seu celular!')
cell.sistema_operacional=input('Digite o sistema do seu celular!')


#executar ações
cell.ligar()
cell.baixar_app()
cell.excluir_app()
cell.desligar()
