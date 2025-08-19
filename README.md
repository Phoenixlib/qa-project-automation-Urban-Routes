# Pruebas Urban Routes

## Descripción del Proyecto

Urban Routes es una aplicación web para solicitar servicios de taxi. Este proyecto contiene un conjunto de pruebas automatizadas que validan el flujo completo de solicitud de taxi, desde la configuración de la ruta hasta la confirmación del pedido.

Las pruebas cubren las siguientes funcionalidades principales:
- Configuración de direcciones de origen y destino
- Selección de tarifa Comfort
- Registro y validación de número de teléfono
- Adición de método de pago (tarjeta de crédito)
- Envío de mensajes al conductor
- Solicitud de servicios adicionales (manta, pañuelos, helado)
- Confirmación del pedido de taxi

## Tecnologías y Técnicas Utilizadas

### Tecnologías
- **Python**: Lenguaje de programación principal
- **Selenium WebDriver**: Framework para automatización de navegadores web
- **Chrome WebDriver**: Driver específico para el navegador Google Chrome
- **pytest**: Framework de testing implícito (basado en la estructura de las clases de prueba)

### Técnicas de Testing
- **Page Object Model (POM)**: Patrón de diseño que encapsula los elementos y acciones de cada página en clases separadas
- **Explicit Waits**: Uso de `WebDriverWait` y `expected_conditions` para sincronización robusta
- **Localizadores múltiples**: Implementación de diferentes estrategias de localización (ID, CSS Selector, XPath, Class Name)
- **Gestión de logs del navegador**: Captura de logs de rendimiento para obtener códigos de verificación SMS
- **Configuración centralizada**: Uso del módulo `data` para centralizar datos de prueba

### Características Técnicas
- **Manejo de ventanas modales**: Interacción con elementos emergentes y modales
- **Simulación de entrada de usuario**: Envío de teclas especiales (`Keys.TAB`)
- **Validación de códigos SMS**: Función especializada para extraer códigos de confirmación telefónica
- **Timeouts configurables**: Esperas de hasta 40 segundos para elementos críticos
- **Setup y Teardown**: Configuración automática del navegador al inicio y limpieza al final

## Instrucciones para Ejecutar las Pruebas

### Prerrequisitos
1. **Python**: Asegúrate de tener Python instalado en tu sistema
2. **Dependencias**: Instala las librerías necesarias:
   ```bash
   pip install selenium
   ```
3. **Chrome WebDriver**: El código utiliza el Service() sin parámetros, por lo que necesitas:
   - Tener Google Chrome instalado
   - ChromeDriver en tu PATH del sistema, o
   - ChromeDriver en la misma carpeta que tu script

4. **Archivo de datos**: El proyecto incluye un archivo `data.py` con la configuración necesaria:
   ```python
   urban_routes_url = 'https://cnt-5e53e537-8e7f-415b-86d8-1b2cce62a582.containerhub.tripleten-services.com?lng=es'
   address_from = 'East 2nd Street, 601'
   address_to = '1300 1st St'
   phone_number = '+1 123 123 12 12'
   card_number, card_code = '1234 5678 9100', '111'
   message_for_driver = 'Muéstrame el museo'
   ```
   **Nota**: Este archivo ya está configurado con datos de prueba válidos para el entorno de Urban Routes.

### Ejecutar las Pruebas

#### Opción 1: Ejecutar con pytest
```bash
pytest main.py -v
```

#### Opción 2: Ejecutar como script de Python
```bash
python main.py
```

#### Opción 3: Ejecutar pruebas individuales
Para ejecutar una prueba específica con pytest:
```bash
pytest main.py::TestUrbanRoutes::test_set_route -v
```

### Orden de Ejecución
Las pruebas están diseñadas para ejecutarse en secuencia, ya que cada prueba depende del estado generado por la anterior:

1. `test_set_route`: Configura las direcciones
2. `test_select_comfort`: Selecciona la tarifa
3. `test_fild_phone_number`: Valida el número de teléfono
4. `test_add_credit_card`: Agrega método de pago
5. `test_message_driver`: Envía mensaje al conductor
6. `test_ask_for_blanket`: Solicita manta y pañuelos
7. `test_ask_ice_cream`: Solicita helado
8. `test_order_taxi`: Confirma el pedido

### Notas Importantes
- Las pruebas requieren acceso a la aplicación Urban Routes en funcionamiento
- El navegador Chrome se abrirá automáticamente durante la ejecución
- Los códigos de verificación SMS se obtienen automáticamente de los logs del navegador
- Las pruebas pueden tardar varios minutos en completarse debido a las esperas y la carga de la aplicación

## Estructura del Proyecto
```
proyecto/
│
├── main.py                  # Archivo principal con las pruebas
├── data.py                  # Archivo de configuración con datos de prueba
└── README.md               # Este archivo
```

## Datos de Prueba Configurados

El archivo `data.py` incluye los siguientes datos de prueba:

- **URL de la aplicación**: Entorno de pruebas de Urban Routes con interfaz en español
- **Direcciones**: 
  - Origen: "East 2nd Street, 601"
  - Destino: "1300 1st St"
- **Número de teléfono**: "+1 123 123 12 12" (formato estadounidense)
- **Tarjeta de crédito**: 
  - Número: "1234 5678 9100"
  - Código CVV: "111"
- **Mensaje para el conductor**: "Muéstrame el museo"

Estos datos están preconfigurados para funcionar con el entorno de pruebas de Urban Routes y no requieren modificación para ejecutar las pruebas.