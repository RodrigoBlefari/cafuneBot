import pyautogui as magic
import time

# O tempo é em segundos

def botStart():
    # EM SEGUNDOS
    tempoDeAviso = 60

    #TEXTO QUE SERÁ EXIBITO
    texto1 = '''\
        MTNÊ #10 terça 28/06
        18h00 - Luhli
        18h30 - Masa
        19h30 - 10zanu
        20h00 - Moita
        20h30 - Silencio
        21h00  - cafuNina / @purpurinina
        21h30 - Random
        22h00 - Buda
        22h30 - Lezza
        23h00 - Patrick
        23h30 - Cran'''
    #TEMPO EM SEGUNDOS, 60*5 = 5 MINUTOS
    tempo1 = 70
    contador1 = tempoDeAviso

    texto2 = "A gente quer as mana livre e a vontade por aqui então se qualquer uma sentir um descoonforto, liga nois que as cafunela tá on <3 passou dos limite, manda la https://bit.ly/passoudoslimites"
    tempo2 = 60*10
    contador2 = tempoDeAviso

    textoBoraFumarUmCafune ="Bora Fumar 1 cafune?"
    tempoFumar = 420
    contadorFumar = tempoDeAviso

    print("Bot Start")
    for i in range(0,9999999999999,+1): 

    ##################TEXTO 1 ###################################

        if i > tempo1 - tempoDeAviso and i <= tempo1:
            contador1 -= 1
            contador(contador1, "Texto 1")
            if contador1 == 0:
                contador1 = tempoDeAviso
        if i == tempo1:
            tempo1 = tempo1 + tempo1
            escrever(texto1)
            
    ##################TEXTO 2 ###################################

        if i > tempo2 - tempoDeAviso and i <= tempo2:
            contador2 -= 1
            contador(contador2, "Texto 2")
            if contador2 == 0:
                contador2 = tempoDeAviso
        if i == tempo2:
            tempo2 = tempo2 + tempo2
            escrever(texto2)
            
    ##################TEXTO FUMAR ###################################

        if i > tempoFumar - tempoDeAviso and i <= tempoFumar:
            contadorFumar -= 1
            contador(contadorFumar, "4:20 em dubai")
            if contadorFumar == 0:
                contadorFumar = tempoDeAviso
        if i == tempoFumar:
            tempoFumar = tempoFumar + tempoFumar
            escrever(textoBoraFumarUmCafune)

        time.sleep(1)

        def escrever(texto):
        
            print(texto)
            # magic.hotkey('alt', 'h')
            # magic.write("CafuBot - " + texto)
            # magic.press('enter')
            # magic.hotkey('alt', 'h')
            # magic.click()

        def contador(segundos, texto):
            print("Proxima msg em " + str(segundos) + " segundos : " + texto)

botStart() 