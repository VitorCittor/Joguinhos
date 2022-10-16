#Um jogo de decisões onde terá vários finais dependendo das suas escolhas

#Você é um aventureiro em um mundo assolado por guerras constantes e precisa escolher entre duas faccões: Saqueadores e Pacificadores. Apenas os Saqueadores irão vencer.





import PySimpleGUI as sg


class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou no sul? (n/s)' #Norte = Saqueadores, Sul = Pacificadores
        self.pergunta2 = 'Você prefere uma espada ou um arco? (espada/arco)' # espada = lado1, arco = lado2
        self.pergunta3 = 'Qual sua especialidade? (linha de frente ou tático)' #linha de frente = lado1, tático = lado2
        self.finalHistoria1 = 'Você foi um héroi na linha de frente e garantiu a vitória!'
        self.finalHistoria2 = 'Você foi um herói de controle e impediu o avanço dos inimigos!'
        self.finalHistoria3 = 'Você fez parte da vanguarda e se sacrificou pelo seu reino!'
        self.finalHistoria4 = 'Suas táticas eram boas, porém não foi suficiente para impedir o avanço do lado inimigo!'
    
    
    
    def Iniciar(self):
        #layout
        layout = [
            [sg.Output(size = (50,10))],
            [sg.Input(size = (25,0), key = 'escolha')],
            [sg.Button('Iniciar'), sg.Button('Responder')]
        ]
        #criar a janela
        self.janela=sg.Window('Jogo de Aventura!',layout =layout)
        while True:
            #ler os dados
            self.LerValores()
            #fazer algo com os dados
            if self.evento == 'Iniciar':    
                print(self.pergunta1)
                self.LerValores()
                if self.valores['escolha'] == 'n':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'espada':
                            print(self.finalHistoria1)
                    if self.valores['escolha'] == 'arco':
                            print(self.finalHistoria2) 
                if self.valores['escolha'] == 's':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'linha de frente':
                        print(self.finalHistoria3)
                    if self.valores['escolha'] == 'tático':
                        print(self.finalHistoria4)    

    def LerValores(self):
        self.evento, self.valores = self.janela.Read()



jogo = JogoDeAventura()
jogo.Iniciar()                
