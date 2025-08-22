# QA Project: Urban Routes App Testing

Este proyecto de control de calidad utiliza el patrón de diseño **Page Object Model (POM)** y la biblioteca **Selenium WebDriver** para automatizar las pruebas de las funcionalidades de la aplicación de taxis **Urban Routes**. El objetivo es asegurar que las características principales de la aplicación web funcionen correctamente, incluyendo la solicitud de rutas, selección de tarifas, métodos de pago, y la interacción con el conductor.

---

## 🚀 Tecnologías Utilizadas

* **Python 3:** Lenguaje de programación principal.
* **Selenium WebDriver:** Biblioteca para la automatización de la interfaz de usuario del navegador.
* **pytest:** Framework de pruebas para ejecutar los tests.
* **Google Chrome:** Navegador utilizado para la ejecución de las pruebas.

---

## 📂 Estructura del Proyecto

El proyecto sigue una estructura clara y organizada bajo el patrón **Page Object Model**.

* `Data/`: Contiene el archivo `data.py` con las constantes y variables de prueba (URLs, direcciones, números de teléfono, etc.).
* `Pages/`: Contiene los objetos de página (`UrbanRoutes.py`), que encapsulan los localizadores web y las interacciones con los elementos de la página.
* `Tests/`: Contiene el archivo `TestUrbanRoutes.py`, donde se encuentran los scripts de prueba. Cada método de prueba valida una funcionalidad específica.
* `Utils/`: Contiene funciones de utilidad, como `phone_code.py`, que se utiliza para obtener el código de confirmación del teléfono de los registros del navegador.
* `README.md`: Este archivo, que documenta el proyecto.

---

## 📝 Descripción de las Pruebas

El archivo `TestUrbanRoutes.py` contiene una suite de pruebas que valida el flujo principal de la aplicación. Los tests cubiertos son:

1.  **`test_set_route`**: Verifica que las direcciones de origen y destino se establecen correctamente en los campos del formulario.
2.  **`test_select_comfort`**: Asegura que el usuario puede seleccionar la tarifa "Comfort".
3.  **`test_fild_phone_number`**: Prueba el proceso de rellenar el número de teléfono y el código de confirmación.
4.  **`test_add_credit_card`**: Valida la funcionalidad de agregar una nueva tarjeta de crédito como método de pago.
5.  **`test_message_driver`**: Confirma que el mensaje para el conductor se agrega exitosamente.
6.  **`test_ask_for_blanket`**: Verifica que la opción de "Manta y pañuelos" se puede seleccionar.
7.  **`test_ask_ice_cream`**: Prueba la funcionalidad del contador de "Helado", asegurando que no se pueda exceder el límite.
8.  **`test_order_taxi`**: Valida que se puede iniciar la solicitud de un taxi.
9.  **`test_wait_driver_found`**: Asegura que el sistema espera y detecta la asignación de un conductor.

---

## 🛠️ Instalación y Ejecución

Para ejecutar estas pruebas, sigue los siguientes pasos:

### 1. Requisitos
* Tener Python 3 instalado.
* Tener **Google Chrome** instalado en tu sistema.

### 2. Instalación de Dependencias
Abre la terminal en la raíz del proyecto e instala las bibliotecas necesarias:

```bash
pip install -r requirements.txt
````

*(Nota: Si no tienes un archivo `requirements.txt`, puedes crearlo con `pip freeze > requirements.txt` después de instalar `selenium` y `pytest`).*

### 3\. Ejecución de las Pruebas

Para correr toda la suite de pruebas, utiliza el siguiente comando en la terminal:

```bash
pytest
```

  * `pytest` detectará automáticamente el archivo `TestUrbanRoutes.py` y ejecutará todos los métodos que comiencen con `test_`.

-----

## ⚙️ Configuración Adicional

  * **`data.py`**: Este archivo es el corazón de la configuración de datos. Puedes modificar las variables como `urban_routes_url`, `address_from`, `phone_number`, etc., para adaptar las pruebas a diferentes escenarios sin necesidad de cambiar los archivos de prueba.

-----

## 🙋‍♂️ Contacto

Para cualquier pregunta o sugerencia, no dudes en contactar al desarrollador del proyecto.

```
```