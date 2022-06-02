Feature: Acciones Yotube

  Scenario: Realizar varias acciones en youtube
    Given Abrir pagina principal de Youtube
    And seleccionar la seccion Explorar
    And seleccionar la opcion Videojuegos
    When direccionar a la pagina videojuegos
    And Visualizar seccion recomendados
    Then Volver a la pagina principal
    And Buscar test automation
    And Comprobar esta la opcion de filtro