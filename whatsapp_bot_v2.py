from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Localização do diretório de usuario do Chrome
chrome_usuario = r'C:\Users\adryan.silva\AppData\Local\Google\Chrome\User Data'

# Configuração das opções do Chrome
chrome_opcao = webdriver.ChromeOptions()
chrome_opcao.add_argument('--user-data-dir=' + chrome_usuario)

# Criação da instância do ChromeDriver
driver = webdriver.Chrome(options=chrome_opcao)

# Navegação para uma página
driver.get('https://web.whatsapp.com/')

# Tempo para carregar a página web
#time.sleep(20)

# Aguarda o usuario fazer login manualmente
input('Escaneie o [QR CODE] caso não esteja logado para continuar e pressione Enter quando abrir o WhatsApp logado...')

# Lista de contatos e mensagem a ser enviada
contatos = ['Guilherme Ti','Douglas TI']
mensagem = 'teste!!!'

# Loop para enviar mensagem para cada contato
for contato in contatos:
    # Campo de busca de "contato" na agenda pela tag data-tab
    campo_busca = driver.find_element(By.XPATH,'//div[@contenteditable="true"][@data-tab="3"]')
    campo_busca.send_keys(contato)
    time.sleep(2)
    campo_busca.send_keys(Keys.ENTER)

    # Campo de "mensagem" para envio pela tag data-tab
    campo_mensgem = driver.find_element(By.XPATH,'//div[@contenteditable="true"][@data-tab="10"]')
    campo_mensgem.send_keys(mensagem)
    campo_mensgem.send_keys(Keys.RETURN)
    time.sleep(5)

# Saída do robô
driver.quit()
