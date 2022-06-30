import pyautogui as magic
import time
import datetime

# O tempo é em segundos

def botStart():

    #TEXTO QUE SERÁ EXIBITO
    texto1 = ""
    #TEMPO EM SEGUNDOS, 60*5 = 5 MINUTOS
    tempo1 = 60*55555555

    texto2 = "A gente quer as mana livre e a vontade por aqui então se qualquer uma sentir um descoonforto, liga nois que as cafunela tá on <3 passou dos limite, manda la https://bit.ly/passoudoslimites"
    tempo2 = 60*60

    textoBoraFumarUmCafune ="Bora Fumar 1 cafune?"
    tempoFumar = 60*60
    tempoFumar = 19

    print("CafuBot Iniciado com sucesso")

    def escrever(texto):

        print(texto)
        magic.hotkey('alt', 'h')
        magic.write("CafuBot - " + texto)
        magic.press('enter')
        magic.hotkey('alt', 'h')
        magic.click()
        time.sleep(1)
            
    for i in range(0,9999999999999,+1): 
        now = datetime.datetime.now()
        minuteNow = '{:02d}'.format(now.minute)
        
    ##################TEXTO 1 ###################################

        if i == tempo1:
            tempo1 = tempo1 + tempo1
            escrever(texto1)
            
    ##################TEXTO 2 ###################################

        if i == tempo2:
            tempo2 = tempo2 + tempo2
            escrever(texto2)
            
    ##################TEXTO FUMAR ###################################
        if int(minuteNow) == int(tempoFumar):
            escrever(textoBoraFumarUmCafune + " 4:20 em dubai Confia")
            # tempoFumar = tempoFumar + tempoFumar
            time.sleep(50)
        time.sleep(1)

botStart() 