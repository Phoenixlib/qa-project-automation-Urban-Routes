import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_tariff = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    phone_number_button = (By.CLASS_NAME, 'np-text')
    insert_phone_number = (By.ID, 'phone')
    send_phone_number = (By.XPATH, '//button[@type="submit" and text()="Siguiente"]')
    sms_code = (By.ID, 'code')
    confirm_sms_code_button = (By.XPATH, '//button[@type="submit" and text()="Confirmar"]')

    pay_method_button = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card_button = (By.XPATH, '//div[@class="pp-title" and text()="Agregar tarjeta"]')
    card_number_input = (By.ID, 'number')
    card_code_input = (By.XPATH, '//input[@id="code" and @class="card-input"]')
    save_card_button = (By.XPATH, '//button[@class="button full" and text()="Agregar"]')
    close_pay_method_modal = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')

    message_driver = (By.ID, 'comment')
    checkbox_blanket = (By.XPATH, '//div[contains(text(), "Manta y pañuelos")]/following-sibling::div//span[@class="slider round"]')

    counter_plus_ice_cream = (By.XPATH, '//div[contains(text(), "Helado")]/following-sibling::div//div[@class="counter-plus"]')
    order_taxi_button = (By.CLASS_NAME, 'smart-button')
    order_number = (By.CLASS_NAME, 'order-number')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def set_from(self, from_address):
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)
    def set_to(self, to_address):
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)
#Seleccionar tarifa comfort
    def get_request_taxi_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.request_taxi_button))

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_tariff(self):
        return self.wait.until(EC.element_to_be_clickable(self.comfort_tariff))
    def click_comfort_tariff(self):
        self.get_comfort_tariff().click()
#Rellenar el numero de telefono
    def get_button_phone_number(self):
        return self.wait.until(EC.element_to_be_clickable(self.phone_number_button))
    def click_button_phone_number(self):
        self.get_button_phone_number().click()
    def get_insert_phone_number(self):
        return self.wait.until(EC.visibility_of_element_located(self.insert_phone_number))
    def set_insert_phone_number(self, phone_number):
        self.get_insert_phone_number().send_keys(phone_number)
    def get_send_phone_number(self):
        return self.wait.until(EC.element_to_be_clickable(self.send_phone_number))
    def click_send_phone_number(self):
        self.get_send_phone_number().click()
    def get_input_sms_code(self):
        return self.wait.until(EC.visibility_of_element_located(self.sms_code))
    def set_input_sms_code(self, code):
        self.get_input_sms_code().send_keys(code)
    def get_confirm_sms_code_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.confirm_sms_code_button))
    def click_confirm_sms_code_button(self):
        self.get_confirm_sms_code_button().click()
#agregar una tarjeta de credito
    def get_pay_method_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.pay_method_button))
    def click_pay_method_button(self):
        self.get_pay_method_button().click()
    def get_add_card_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_card_button))
    def click_add_card_button(self):
        self.get_add_card_button().click()
    def get_card_number_input(self):
        return self.wait.until(EC.visibility_of_element_located(self.card_number_input))
    def set_card_number_input(self, card_number_input):
        self.get_card_number_input().send_keys(card_number_input)
    def get_card_code_input(self):
        return self.wait.until(EC.visibility_of_element_located(self.card_code_input))
    def set_card_code_input(self, card_code_input):
        card_field = self.get_card_code_input()
        card_field.send_keys(card_code_input)
        card_field.send_keys(Keys.TAB)
    def get_save_card_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_card_button))
    def click_save_card_button(self):
        self.get_save_card_button().click()
    def get_close_pay_method_modal(self):
        return self.wait.until(EC.visibility_of_element_located(self.close_pay_method_modal))
    def click_close_pay_method_modal(self):
        self.get_close_pay_method_modal().click()
#mensaje al conductor
    def get_input_message_driver(self):
        return self.wait.until(EC.presence_of_element_located(self.message_driver))
    def set_message_driver(self, message_driver):
        self.get_input_message_driver().send_keys(message_driver)
#pedir manta y pañuelos
    def get_checkbox_blanket(self):
        return self.wait.until(EC.presence_of_element_located(self.checkbox_blanket))
    def click_checkbox_blanket(self):
        self.get_checkbox_blanket().click()
#pedir helado
    def get_ice_cream(self):
        return self.wait.until(EC.presence_of_element_located(self.counter_plus_ice_cream))
    def click_counter_plus_ice_cream(self):
        self.get_ice_cream().click()
#pedir taxi
    def get_order_taxi(self):
        return self.wait.until(EC.element_to_be_clickable(self.order_taxi_button))
    def click_order_taxi(self):
        self.get_order_taxi().click()
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(self.order_number))
#getter setter reader clicker

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("goog:loggingPrefs",{'performance':'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_select_comfort(self):
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_tariff()

    def test_fild_phone_number(self):
        self.routes_page.click_button_phone_number()
        self.routes_page.set_insert_phone_number(data.phone_number)
        self.routes_page.click_send_phone_number()
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_input_sms_code(code)
        self.routes_page.click_confirm_sms_code_button()

    def test_add_credit_card(self):
        self.routes_page.click_pay_method_button()
        self.routes_page.click_add_card_button()
        self.routes_page.set_card_number_input(data.card_number)
        self.routes_page.set_card_code_input(data.card_code)
        self.routes_page.click_save_card_button()
        self.routes_page.click_close_pay_method_modal()

    def test_message_driver(self):
        self.routes_page.set_message_driver(data.message_for_driver)

    def test_ask_for_blanket(self):
        self.routes_page.click_checkbox_blanket()

    def test_ask_ice_cream(self):
        for _ in range(2):
            self.routes_page.click_counter_plus_ice_cream()

    def test_order_taxi(self):
        self.routes_page.click_order_taxi()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
