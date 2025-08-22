from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

    checkbox_blanket = (By.XPATH, '//div[contains(text(), "Manta y pañuelos")]/following-sibling::div//input[@class="switch-input"]')
    span_checkbox_blanket = (By.XPATH, '//div[contains(text(), "Manta y pañuelos")]/following-sibling::div//span[@class="slider round"]')
    counter_plus_ice_cream = (By.XPATH, '//div[contains(text(), "Helado")]/following-sibling::div//div[@class="counter-plus"]')
    counter_plus_disabled = (By.XPATH, '//div[contains(text(), "Helado")]/following-sibling::div//div[contains(@class, "counter-plus") and contains(@class, "disabled")]')
    order_taxi_button = (By.CLASS_NAME, 'smart-button')
    order_number = (By.CLASS_NAME, 'order-number')
    detalles_button = (By.XPATH, '//div[text()="Detalles"]')
# asserts
    comfort_assert = (By.XPATH, '//div[@class="r-sw-label" and contains(text(), "Manta y pañuelos")]')
    added_card = (By.XPATH, '//div[@class="pp-title" and text()="Tarjeta"]')
    order_visible = (By.CLASS_NAME, 'order-header-title')

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
    #assert
    def is_comfort_selected(self):
        element = self.wait.until(EC.presence_of_element_located(self.comfort_assert))
        return element.text
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
    #assert
    def is_number_write(self):
        element = self.driver.find_element(*self.insert_phone_number).get_property('value')
        return element
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
    #assert
    def card_title_displayed(self):
        element = self.wait.until(EC.presence_of_element_located(self.added_card))
        return element.is_displayed()
#mensaje al conductor
    def get_input_message_driver(self):
        return self.wait.until(EC.presence_of_element_located(self.message_driver))
    def set_message_driver(self, message_driver):
        self.get_input_message_driver().send_keys(message_driver)
    #assert
    def message_driver_added(self):
        element = self.driver.find_element(*self.message_driver).get_property('value')
        return element
#pedir manta y pañuelos
    def get_span_checkbox_blanket(self):
        return self.wait.until(EC.presence_of_element_located(self.span_checkbox_blanket))
    def get_checkbox_blanket(self):
        return self.wait.until(EC.presence_of_element_located(self.checkbox_blanket))
    def click_span_checkbox_blanket(self):
        self.get_span_checkbox_blanket().click()
#pedir helado
    def get_ice_cream(self):
        return self.wait.until(EC.presence_of_element_located(self.counter_plus_ice_cream))
    def get_counter_plus_disabled(self):
        return self.wait.until(EC.presence_of_element_located(self.counter_plus_disabled))
    def click_counter_plus_ice_cream(self):
        self.get_ice_cream().click()

#pedir taxi
    def get_order_taxi(self):
        return self.wait.until(EC.element_to_be_clickable(self.order_taxi_button))
    def click_order_taxi(self):
        self.get_order_taxi().click()
    def get_order_visible(self):
        element = self.wait.until(EC.visibility_of_element_located(self.order_visible))
        return element.is_displayed()
    def wait_driver_found(self):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(self.order_number))
    def get_detalles_btn(self):
        element = self.wait.until(EC.visibility_of_element_located(self.detalles_button))
        return element.is_displayed()
        #getter setter reader clicker