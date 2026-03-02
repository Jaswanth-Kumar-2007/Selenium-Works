from Booking import constants as const
from Booking.booking_filtration  import BookingFiltration
from Booking.booking_report import BookingReport

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Booking(webdriver.Edge):
    def __init__(self,teardown = False):
        self.teardown = teardown
        super(Booking,self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self,currency = None):
        currency_element = self.find_element(
            By.CSS_SELECTOR,'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()

        selected_currency_element = self.find_element(
            By.XPATH, f'//div[text()="{currency}"]'
        )
        selected_currency_element.click()

    def select_place_to_go(self,place_to_go):
        search_field = self.find_element(By.NAME,'ss')
        search_field.clear()
        search_field.send_keys(place_to_go)
        time.sleep(5)
        first_result = self.find_element(
            By.CSS_SELECTOR,'li[id="autocomplete-result-0"]'
        )
        first_result.click()
        
    def select_dates(self,check_in_date,check_out_date):
        check_in_element = self.find_element(
            By.CSS_SELECTOR,f'td[data-date]="{check_in_date}]'
        )
        check_in_element.click()

        check_out_element = self.find_element(
            By.CSS_SELECTOR,f'td[data-date]="{check-check_out_date}"]'
        )
        check_out_element.click()

    def select_adults(self,count = 1):
        selection_element = self.find_element(
            By.ID,'xp__guests__toggle'
        )
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element(
                By.CSS_SELECTOR,'button[aria-label="Decrease number of Adults"]'
            )

            decrease_adults_element.click()

            adults_value_element = self.find_element(By.ID,'group_adults')
            adults_value = adults_value_element.get_attribute(
                'value'
            )

            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element(
            By.CSS_SELECTOR,'button[aria-label="Increase number of Adults"]'
        )

        for i in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element(
            By.CSS_SELECTOR,'button[type="submit]'
        )
        search_button.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(3,4,5)
        filtration.sort_price_lowest_first()

    def report_results(self):
        hotel_boxes = self.find_element(By.ID,'hotellist_inner').find_element(By.CLASS_NAME,'sr_proprty_block')

        report = BookingReport(hotel_boxes)
        print(report.pull_deal_box_attributes())
