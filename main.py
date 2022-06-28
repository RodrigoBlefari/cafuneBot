import pyautogui as magic
import time

# O tempo é em segundos

def botStart():
    print("Bot Start")

    textoPix = "Gostando do programa? Faca um pix pra nossa querida Narosa <3 contatochadebuceta@gmail.com"
    tempoPix = 10

    textoAssedio = "a gente quer as mana livre e a vontade por aqui então se qualquer uma sentir um descoonforto, liga nois que as cafunela tá on <3 passou dos limite, manda la https://bit.ly/passoudoslimites"
    tempoAssedio = 20

    textoBoraFumarUmCafune ="Bora Fumar 1 cafune?"
    tempooBoraFumarUmCafun = 30

    for i in range(0,9999999999999,+1): 

        if i == tempoPix:
            tempoPix = tempoPix + tempoPix
            
            TextoPix(textoPix)

        if i == tempoAssedio:
            tempoAssedio = tempoAssedio + tempoAssedio
            TextoAssedio(textoAssedio)

        if i == tempooBoraFumarUmCafun:
            tempooBoraFumarUmCafun = tempooBoraFumarUmCafun + tempooBoraFumarUmCafun
            TextoFumar(textoBoraFumarUmCafune)

        time.sleep(1)

def TextoPix(textoPix):
    
    print("Texto Pix")
    magic.hotkey('alt', 'h')
    magic.write("CafuBot - " + textoPix)
    magic.press('enter')
    magic.hotkey('alt', 'h')
    magic.click()

def TextoAssedio(textoAssedio):
    
    print("Texto Assedio")
    magic.hotkey('alt', 'h')
    magic.write("CafuBot - " + textoAssedio)
    magic.press('enter')
    magic.hotkey('alt', 'h')
    magic.click()
   
def TextoFumar(textoBoraFumarUmCafune):
    
    print("Texto Fumar! ")
    magic.hotkey('alt', 'h')
    magic.write("CafuBot - " + textoBoraFumarUmCafune)
    magic.press('enter')
    magic.hotkey('alt', 'h')
    magic.click()

botStart()       
