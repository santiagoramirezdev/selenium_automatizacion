import time
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def automatizacion(eleccion):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if eleccion == '1':
        correo = input(f"ingrese el correo para el registro\n")
        password = "Xana123456"
        primer_nombre = "Santiago"
        apellido = "Ramirez"
        fecha_de_nacimiento = "20/03/1994"
        driver.get('https://www.instant-gaming.com/es')
        driver.maximize_window()
        #driver.implicitly_wait(15)
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
        time.sleep(10)

if __name__ == '__main__':
    eleccion = input(f"selecciones una opcion para hacer con el programa \n"
                     f"1 --> registro en instant gamming \n"
                     f"2 --> compra de un producto \n"
                     f"3 --> busqueda ed un producto \n")

    automatizacion(eleccion)