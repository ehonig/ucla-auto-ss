from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import keyring
from cryptography.fernet import Fernet
from time import sleep

def get_login_info(fernet_key, user_key, system):
    fernet = Fernet(fernet_key)
    usr = fernet.decrypt(keyring.get_password(system, user_key)[2:-1].encode()).decode()
    pwd = fernet.decrypt(keyring.get_password(system, usr)[2:-1].encode()).decode()
    return usr, pwd

wait = lambda id, driver, wait_time = 10: WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.ID, id)))
click_js = lambda id, driver: driver.execute_script("arguments[0].click();", driver.find_element_by_id(id))

def sleep_and_scroll(driver, sleep_time = 1):
    sleep(sleep_time)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # driver.find_element_by_tag_name('html').send_keys(Keys.END)

def move_driver_forward(id, driver, wait_time=10):
    sleep_and_scroll(driver)
    wait(id, driver, wait_time)
    click_js(id, driver)
    click_js('NextButton', driver)

def auto_survey(fernet_key = 'your fernet key', user_key = 'your user key', system = 'your system'):
    usr, pwd = get_login_info(fernet_key, user_key, system)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome('chromedriver.exe', options = chrome_options)

    driver.get('https://uclasurveys.co1.qualtrics.com/jfe/form/SV_3qRLtouCYKzBbH7')
    move_driver_forward('QID3-2-label', driver) # student/student employee option
    # UCLA login
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.ID, "logon")))
    driver.find_element_by_id('logon').send_keys(usr)
    driver.find_element_by_id('pass').send_keys(pwd)
    driver.find_element_by_class_name('primary-button').click()
    # DUO authenticate at this point
    move_driver_forward('QID260-2-label', driver, 1000)
    sleep_and_scroll(driver)
    wait("NextButton", driver)
    click_js('NextButton', driver)
    move_driver_forward('QID215-2-label', driver)
    move_driver_forward('QID207-4-label', driver)
    # going to campus
    move_driver_forward('QID2-1-label', driver)
    # symptoms
    move_driver_forward('QID12-2-label', driver)
    try:
        move_driver_forward('QID289-2-label', driver, 3)
    except TimeoutException:
        # waiting for test
        move_driver_forward('QID293-1-label', driver, 1)
    finally:
        driver.quit()

if __name__ == "__main__":
    auto_survey()
