import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.explorePage import *
from pages.searchPage import *
from pages.videogamePage import *
from pages.homePage import *
from functions.inicializar import inicializar

URL = inicializar.URL
class functions(inicializar):

    def abrir_navegador(self, navegador=inicializar.NAVEGADOR):

        if navegador == ("CHROME"):
            self.driver = webdriver.Chrome(executable_path="C:\\Users\sfernan9\PycharmProjects\Test4Selenium\\resources\drivers\chromedriver_win\chromedriver.exe")
            self.driver.get(URL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30)
            self.driver.find_element(By.XPATH, inicio.btn_aceptar).click()
            return self.driver

        if navegador == ("FIREFOX"):
            self.driver = webdriver.Firefox(
                executable_path="C:\\Users\sfernan9\PycharmProjects\Test4Selenium\\resources\drivers\geckodriver\geckodriver.exe")
            self.driver.get(URL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30)
            self.driver.find_element(By.XPATH, inicio.btn_aceptar).click()
            return self.driver

        elif navegador!= ("CHROME") and ("FIREFOX"):
            print("----------------")
            print("Define el DRIVER")
            print("----------------")
            exit

    def tear_Down(self):
        print("Se cerrará  el DRIVER")
        self.driver.quit()


    def abrirExplorador(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, inicio.btn_explorar).click()


    def selectVideojuegos(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, explo.btn_videojuegos).click()

    def comprobarTitulo(self):
        time.sleep(2)
        textTitle = self.driver.find_element(By.XPATH, videogame.titulo_page).text
        print("El titulo es " + textTitle)
        if textTitle == videogame.txt_titulo:
            return True

    def comprobarSec(self):
        texto = self.driver.find_element(By.XPATH, videogame.titulo_sec).text
        print("El titulo es " + texto)
        if texto == videogame.txt_secundario:
            return True

    def backHome(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,videogame.btn_inicio).click()

    def buscar(self):
        time.sleep(1)
        self.driver.find_element(By.NAME, inicio.input_buscador).click()
        self.driver.find_element(By.NAME, inicio.input_buscador).send_keys("test automation")
        self.driver.find_element(By.ID, inicio.logo_buscador).click()

    def is_display_filtros(self):
        filtros = self.driver.find_element(By.XPATH, searchtest.opc_filtro).is_displayed()
        print(filtros)
        assert filtros is True
        time.sleep(1)


    def verificar_texto_xpath_titulo(self):  # devuelve true o false
        try:
            wait = WebDriverWait(self.driver, 15)
            wait.until(EC.text_to_be_present_in_element((By.XPATH, videogame.titulo_page), videogame.txt_titulo))
        except NoSuchElementException:
            print(u"Verificar Texto: No presente Xpath" + videogame.titulo_page + " el texto, " + videogame.txt_titulo)
            # self.driver.close()
            functions.tearDown(self)
        print(u"Verificar Texto: Se visualizó en, " + videogame.titulo_page + " el texto, " + videogame.txt_titulo)
        return True

    # No funciona
    def ir_a_xpath(self):
        try:
            localizador = self.driver.find_element(By.XPATH, videogame.titulo_sec)
            self.driver.execute_script("arguments[0].scrollIntoView();", localizador)

        except TimeoutException:

            print(u"ir_a_xpath: No presente " + videogame.titulo_page)
            functions.tearDown(self)

        print(u"ir_a_xpath: Se desplazÃ³ al elemento, " + videogame.titulo_page)
        return True