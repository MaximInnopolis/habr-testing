import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

class Login:

    email = (By.ID, "email_field")
    password = (By.ID, "password_field")
    login_btn = (By.NAME, "go")
    error = (By.CSS_SELECTOR, ".notice.error .notice__text")
    login_page_btn = (By.CSS_SELECTOR, ".btn.btn_solid.btn_small.tm-header-user-menu__login")
    # recaptcha_checkbox = (By.ID, "recaptcha-anchor")

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login_page(self):
        login_page_btn_ele = self.driver.find_element(*self.login_page_btn)
        login_page_btn_ele.click()

    def enter_email(self, email):
        email_ele = self.driver.find_element(*self.email)
        email_ele.send_keys(email)

    def enter_password(self, password):
        password_ele = self.driver.find_element(*self.password)
        password_ele.send_keys(password)

    def click_login(self):
        login_ele = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.login_btn)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", login_ele)
        try:
            login_ele.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", login_ele)

    # def solve_recaptcha(self):
    #     try:
    #         recaptcha_frame = WebDriverWait(self.driver, 20).until(
    #             EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title='reCAPTCHA']"))
    #         )
    #         self.driver.switch_to.frame(recaptcha_frame)
    #         recaptcha_checkbox_ele = WebDriverWait(self.driver, 20).until(
    #             EC.element_to_be_clickable(self.recaptcha_checkbox)
    #         )
    #         recaptcha_checkbox_ele.click()
    #         self.driver.switch_to.default_content()
    #         time.sleep(5)
    #     except TimeoutException:
    #         print("Timeout while solving reCAPTCHA.")
    #     except Exception as e:
    #         print(f"Error solving reCAPTCHA: {e}")

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        # self.solve_recaptcha()
        self.click_login()
        time.sleep(3)

    def error_msg(self):
        wait = WebDriverWait(self.driver, 20)
        error_ele = wait.until(EC.presence_of_element_located(self.error))
        return error_ele.text
