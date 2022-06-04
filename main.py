import time
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



def automatizacion(eleccion):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.instant-gaming.com/es')
    driver.maximize_window()
    if eleccion == '1':
        correo = input(f"ingrese el correo para el registro\n")
        password = "Xana123456"
        primer_nombre = "Santiago"
        apellido = "Ramirez"
        fecha_de_nacimiento = "20/03/1994"
        menu = driver.find_element(By.CLASS_NAME, "burger")
        menu.click()
        link_registro = driver.find_element(By.ID, "register-manual")
        link_registro.click()
        time.sleep(3)
        print("se procede a llenar los datos")
        campo_email = driver.find_element(By.ID, "ig-email")
        campo_email.send_keys(correo)
        time.sleep(1)
        campo_pass = driver.find_element(By.ID,"ig-pass")
        campo_pass.send_keys(password)
        time.sleep(1)
        campo_nombre = driver.find_element(By.ID, "ig-firstname")
        campo_nombre.send_keys(primer_nombre)
        time.sleep(1)
        campo_apellido = driver.find_element(By.ID,"ig-lastname")
        campo_apellido.send_keys(apellido)
        time.sleep(1)
        campo_fecha_nacimiento = driver.find_element(By.ID,"ig-birthdate")
        campo_fecha_nacimiento.send_keys(fecha_de_nacimiento)
        time.sleep(1)
        campo_check_mark = driver.find_element(By.XPATH, "//div[@class='consent darker']/label[2]/span")
        campo_check_mark.click()
        time.sleep(1)
        print("se procede a aceptar")
        btn_aceptar = driver.find_element(By.XPATH, "//button[@class='g-recaptcha button']")
        btn_aceptar.click()
        time.sleep(5)
    elif eleccion == '2':
        nombre_completo = "Santiago Ramirez"
        direccion_facturacion = "calle falsa"
        tarjeta ="111111111111111"
        fecha_expiracion ="03/02"
        primer_juego = driver.find_element(By.ID,"ig-preorders-item-1")
        primer_juego.click()
        time.sleep(2)
        btn_comprar = driver.find_element(By.XPATH,"//div[@class='panel item wide']/div[5]/a[2]")
        btn_comprar.click()
        time.sleep(2)
        campo_nombre_completo = driver.find_element(By.XPATH,"//div[@class='address-form raw']/label[1]/input[@name ='fullname']")
        campo_nombre_completo.send_keys(nombre_completo)
        time.sleep(1)
        campo_direccion_facturacion = driver.find_element(By.XPATH, "//div[@class='address-form raw']/label[2]")
        campo_direccion_facturacion.send_keys(direccion_facturacion)
        time.sleep(1)
        time.sleep(5)
    elif eleccion == '3':
        actions = ActionChains(driver).key_down(Keys.LEFT_ALT).send_keys('s')
        actions.perform()
        time.sleep(2)
        campo_sistemas = driver.find_element(By.XPATH,"//span[@class='select2-selection select2-selection--single']")
        campo_sistemas.click()
        time.sleep(1)
        sub_campo_sistemas = driver.find_element(By.XPATH,"//input[@class='select2-search__field']")
        sub_campo_sistemas.send_keys('pc')
        time.sleep(1)
        campo_genero = driver.find_element(By.XPATH,"//span[@class='select2-selection select2-selection--multiple textarea-search']")
        campo_genero.send_keys('Carreras')
        time.sleep(1)
        actions = ActionChains(driver).key_down(Keys.ENTER)
        actions.perform()
        time.sleep(5)

if __name__ == '__main__':
    eleccion = input(f"selecciones una opcion para hacer con el programa \n"
                     f"1 --> registro en instant gamming \n"
                     f"2 --> compra de un producto \n"
                     f"3 --> busqueda de un producto \n")

    automatizacion(eleccion)