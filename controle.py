import pyautogui
import time
import pandas as pd


pyautogui.PAUSE = 1

# Passo 1 - Acessar o sistema da empresa

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.hotkey("ctrl", "t")
pyautogui.write(
    "https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")
time.sleep(5)

# Passo 2 - Fazer login no sistema

pyautogui.click(x=983, y=441)
pyautogui.write("meu login")
pyautogui.click(x=912, y=529)
pyautogui.write("minha senha")
pyautogui.click(x=1036, y=609)
time.sleep(5)

# Passo 3 - Baixar a base de dados

pyautogui.click(x=504, y=440)
pyautogui.click(x=872, y=212)
pyautogui.click(x=990, y=628)

# Passo 4 - Calcular os indicadores

# importando base de dados
tabela = pd.read_csv(
    r"C:\wamp64\www\automacaoSistemaProcesso\Compras.csv", sep=";")
print(tabela)

# total gasto -> somar colunar Valor Final
totalGasto = tabela["ValorFinal"].sum()

# quantidade -> somar coluna quantidade
quantidade = tabela["Quantidade"].sum()

# preço medio -> total gasto / quantidade
precoMedio = totalGasto / quantidade

print(totalGasto)
print(quantidade)
print(precoMedio)

# Passo 5 - Enviar o email para o diretor/chefe

# entrar no e-mail
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")
time.sleep(5)

# clicar em escrever
pyautogui.click(x=135, y=224)

# preencher o email
pyautogui.write("isasilva123ptc@gmail.com")
pyautogui.press("tab")  # selecionando email
pyautogui.press("tab")  # passar para o campo do assunto
pyautogui.write("Relatório de compras")
pyautogui.press("tab")  # passar pro corpo do email
texto = """
Prezados,
Segue o relatório de compras

Total gasto: {totalGasto:,.2f}
Quantidade de produtos: {quantidade:,}
Preço médio: {precoMedio:,.2f}

Alt.
Isa
"""
pyautogui.write(texto)
pyautogui.hotkey("ctrl", "v")

# enviar
pyautogui.hotkey("ctrl", "enter")
