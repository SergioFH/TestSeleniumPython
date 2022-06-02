from behave import *
from functions.functions import functions as Selenium


@given(u'Abrir pagina principal de Youtube')
def step_impl(self):
    Selenium.abrir_navegador(self)


@given(u'seleccionar la seccion Explorar')
def step_impl(self):
    Selenium.abrirExplorador(self)


@given(u'seleccionar la opcion Videojuegos')
def step_impl(self):
    Selenium.selectVideojuegos(self)


@when(u'direccionar a la pagina videojuegos')
def step_impl(self):
    assert Selenium.comprobarTitulo(self) is True


@when(u'Visualizar seccion recomendados')
def step_impl(self):
    assert Selenium.comprobarSec(self) is True



@then(u'Volver a la pagina principal')
def step_impl(self):
    Selenium.backHome(self)


@then(u'Buscar test automation')
def step_impl(self):
    Selenium.buscar(self)


@then(u'Comprobar esta la opcion de filtro')
def step_impl(self):
    Selenium.is_display_filtros(self)
    Selenium.tear_Down(self)
