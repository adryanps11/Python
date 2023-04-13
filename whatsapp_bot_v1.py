from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

print('\n\33[1;93m<<<------INICIANDO BOT WHATSAPP V1------>>>\33[m\n')

# Criação da instância do ChromeDriver
driver = webdriver.Chrome()

# Navegação para uma página
driver.get('https://web.whatsapp.com')

# Aguarda o usuario fazer login manualmente caso não esteja logado
print('\n\33[1:93m<<<------Escaneie o [QR CODE] caso não esteja logado para continuar e pressione Enter quando abrir o WhatsApp logado------>>>\33[m\n')

# Time para abrir o próximo find
time.sleep(20)

# Campo de busca de "contato" na agenda pela tag data-tab
campo_busca = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
campo_busca.send_keys('Anotações')
time.sleep(2)
campo_busca.send_keys(Keys.ENTER)

# Ação na ferramento de anexos "CLIP"
clip = driver.find_element(By.XPATH,'//div[@title="Anexar"]')
clip.click()

# Tempo para executar a ação e ir para próxima etapa..
time.sleep(3)

# Selecionar o arquivo desejado pelo FIND
anexo = driver.find_element(By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
anexo.send_keys("C:/users/adryan.silva/Documents/Estudos/Power BI/pets/Logo.png")

# Tempo para procurar o arquivo
time.sleep(2)

# Buscar campo de envio em seguida executar o evento de clicar
campo_enviar = driver.find_element(By.XPATH, '//span[@data-testid="send"]')
campo_enviar.click()

# Tempo após o click para carregar a imagem ou arquivo e terminar o envio corretamente.
time.sleep(5)

# Sair do sistema
driver.quit()

#message_box = driver.find_element(By.XPATH,'//div[@contenteditable="true"][@data-tab="10"]')
#message_box.send_keys('Sua mensagem aqui')
#message_box.send_keys(Keys.RETURN)


