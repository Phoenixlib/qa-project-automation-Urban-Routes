from Data import data
from Pages import UrbanRoutes as urp
from utils import phone_code as PC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestUrbanRoutes:

    driver = None



    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("goog:loggingPrefs",{'performance':'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urp.UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_select_comfort(self):
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_tariff()
        actual_text = self.routes_page.is_comfort_selected()
        assert actual_text == 'Manta y pañuelos'

    def test_fild_phone_number(self):
        self.routes_page.click_button_phone_number()
        self.routes_page.set_insert_phone_number(data.phone_number)
        self.routes_page.click_send_phone_number()
        code = PC.retrieve_phone_code(self.driver)
        self.routes_page.set_input_sms_code(code)
        self.routes_page.click_confirm_sms_code_button()
        actual_number = self.routes_page.is_number_write()
        assert actual_number == data.phone_number, "El numero es distinto al que se debia ingresar"

    def test_add_credit_card(self):
        self.routes_page.click_pay_method_button()
        self.routes_page.click_add_card_button()
        self.routes_page.set_card_number_input(data.card_number)
        self.routes_page.set_card_code_input(data.card_code)
        self.routes_page.click_save_card_button()
        assert self.routes_page.card_title_displayed(), "La tarjeta no se muestra después de agregarla"
        self.routes_page.click_close_pay_method_modal()

    def test_message_driver(self):
        self.routes_page.set_message_driver(data.message_for_driver)
        assert self.routes_page.message_driver_added() == data.message_for_driver

    def test_ask_for_blanket(self):
        self.routes_page.click_span_checkbox_blanket()
        checkbox = self.routes_page.get_checkbox_blanket()
        assert checkbox.is_selected()

    def test_ask_ice_cream(self):
        for _ in range(2):
            self.routes_page.click_counter_plus_ice_cream()
        counter_plus = self.routes_page.get_counter_plus_disabled()
        class_attribute = counter_plus.get_attribute("class")
        assert "disabled" in class_attribute, "el símbolo de sumar no se ha desactivado, lo que significa que no se sumaron 2 helados"

    def test_order_taxi(self):
        self.routes_page.click_order_taxi()
        assert self.routes_page.get_order_visible(), "El modal de búsqueda de taxis no ha aparecido"
    def test_wait_driver_found(self):
        self.routes_page.wait_driver_found()
        assert self.routes_page.get_detalles_btn(), "El conductor no se ha mostrado en el modal"
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
