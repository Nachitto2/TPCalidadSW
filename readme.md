# Automatización de prueba unitaria
Este repositorio contiene la automatización de una prueba representativa de interfaz de
usuario (UI) para el flujo de autenticación, desarrollado como parte del trabajo práctico 
de la materia de 
calidad de software.

Las pruebas están construidas utilizando Python y Playwright, enfocándose en validar 
el comportamiento del sistema desde la perspectiva del usuario final (Caja Negra).

El proyecto cubre el camino feliz del ingreso mediante el correo electrónico

### Caso de Prueba: Login Exitoso con Email Válido
* **Descripción:** Verifica que un usuario legítimo pueda ingresar su correo y avanzar en el
 flujo sin ser bloqueado.
* **Datos de Entrada (Input):** `a123@uade.edu.ar`
* **Lógica de Validación:** Se utiliza una aserción negativa. El test comprueba que el 
sistema procesa la solicitud exitosamente validando la ausencia del mensaje "Correo 
electrónico ingresado no válido." en la interfaz, permitiendo al usuario avanzar a la 
validación de seguridad (Captcha).

