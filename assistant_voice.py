apresentacao = """
<speak xml:lang="pt-BR" version="1.0">
Olá, <prosody rate="slow">estou falando mais devagar agora</prosody>. <break time="500ms"/> 
Você pode <emphasis level="strong">enfatizar</emphasis> certas palavras para dar mais expressão à fala. 
Eca! Eu vi uma barata!<break time="500ms"/> Será que tem <prosody pitch="high">ratos</prosody> também?
</speak>
"""


import os
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# Insira suas credenciais aqui
api_key = 'ieDN6HUXPuW_5_Ib7bmI_JyU2B3P1c7316imr3CCgFae'  
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/52ad33ee-7af4-4b36-9409-58b0a378fded'

# Inicializar o autenticador
authenticator = IAMAuthenticator(api_key)

# Inicializar o serviço do Text to Speech
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)
text_to_speech.set_service_url(url)
 

# Configuração da solicitação
response = text_to_speech.synthesize(
    text=apresentacao,
    voice='pt-BR_IsabelaV3Voice',  # Escolha a voz desejada
    accept='audio/wav'  # Formato do áudio de saída
).get_result()

# Salvar o áudio em um arquivo
with open('output.wav', 'wb') as audio_file:
    audio_file.write(response.content)
    print("Áudio convertido com sucesso e salvo em 'output.wav'.")

os.system("play ./output.wav")

quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument('--disable-gpu') 
options.add_argument('--no-sandbox') 
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')


from selenium.webdriver.chrome.service import Service
service = Service(executable_path=r'/usr/lib/chromium-browser/chromedriver')
driver = webdriver.Chrome(service=service, options=options)  

html_code = """
<html>
    <script src="https://code.responsivevoice.org/responsivevoice.js?key=K2ywPf2G"></script>
</html>
"""

driver.get("data:text/html;charset=utf-8," + html_code)

import time
ActionChains(driver).key_down(Keys.F12).key_up(Keys.F12).perform()
driver.execute_script(f"responsiveVoice.speak('{apresentacao}', 'Brazilian Portuguese Female');")
time.sleep(50)  
driver.quit()
