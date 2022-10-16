

import random
import PySimpleGUI as sg

class ChuteONUmero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
        
    def Iniciar(self):
        #layout
        layout = [
            [sg.Text('Seu chute', size=(39,0))],
            [sg.Input(size = (18,0),key = 'ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size = (39,10))]
        ]
        #criar uma janela
        self.janela = sg.Window('Chute o Número!', layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                #receber valores
                self.evento, self.valores = self.janela.Read()
                #tratar os valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo! ')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto!')    
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('Parabéns, você acertou')
                            break
                            
        except:
            print('favor digitar apenas números!')
            self.Iniciar()            
    
    
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)  


chute = ChuteONUmero()
<<<<<<< HEAD
chute.Iniciar() 
=======
chute.Iniciar() 
>>>>>>> e993bb768899ea3907545f62055f02e17545e509
