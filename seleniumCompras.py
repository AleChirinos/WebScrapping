import random
from time import sleep
from selenium import webdriver

busqueda = input("Ingrese su busqueda\n")
sleep(8)
driver = webdriver.Chrome('./chromedriver.exe')

""" driver.get('https://www.olx.com.ec/autos_c378')

boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
for i in range(3): 
    try:
        boton.click()
        sleep(random.uniform(8.0, 10.0))
        boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    except:
        break

autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

for auto in autos:
    precio = auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    print (precio)
    descripcion = auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    print (descripcion) """

###########################################
#Amazon
driver.get('https://www.amazon.com/')
#Solicitar la busqueda
buscadorAmazonTextBox = driver.find_element_by_id('twotabsearchtextbox')
buscadorAmazonTextBox.send_keys(busqueda)
sleep(5)
buscadorAmazonBoton= driver.find_element_by_id('nav-search-submit-button')
buscadorAmazonBoton.click()
sleep(7)
#Recolectar informacion
nombreProductoAmazonText = driver.find_element_by_xpath('//div[@data-component-type="s-search-result"][1]//h2/a/span')
precioEnteroProductoAmazonText= driver.find_element_by_xpath('//div[@data-component-type="s-search-result"][1]//span[@class="a-price-whole"]')
precioFraccionProductoAmazonText= driver.find_element_by_xpath('//div[@data-component-type="s-search-result"][1]//span[@class="a-price-fraction"]')
imagenProductoAmazoniImg= driver.find_element_by_xpath('//div[@data-component-type="s-search-result"][1]//img')

nombreProductoAmazon= nombreProductoAmazonText.text
precioProductoAmazon= float(precioEnteroProductoAmazonText.text) + (float(precioFraccionProductoAmazonText.text)/100)
urlImagenProductoAmazon = imagenProductoAmazoniImg.get_attribute('src')

print(nombreProductoAmazon)
print(precioProductoAmazon)
print(urlImagenProductoAmazon)