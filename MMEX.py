from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
import os

def func(project):
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--disable-dev-shm-using")
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.headless = True
    path = os.getcwd()
    driver = webdriver.Chrome(executable_path=f"{path}/chromedriver.exe")

    driver.get('https://pva.app.intel.com/mmex/test_population/')

    inputElems = driver.find_elements(by=By.CSS_SELECTOR, value='#id_Available_Cycles')

    print(inputElems)
    for inputElem in inputElems:
        inputElem.send_keys(f"{project}")
        inputElem.send_keys(Keys.TAB);
        element = driver.find_element(by=By.CSS_SELECTOR, value='#btnSubmit')
        action = ActionChains(driver)
        action.click(on_element=element)
        action.perform()

# Scrap and save the Azure Trigger URL upon successful job
        element = driver.find_element(by=By.XPATH, value="(//*[text()='Job Details'])")
        url = element.get_attribute('href')
        driver.close()

# Save scrapped URL into text
    today = date.today()
    print(f'{project}-{today}')
    my_file = Path(f'C:/SVSHARE/MMEX_Populater/Selenium/Test-Population/{today}')
    try:
        if my_file.is_dir():
            pass
        else:
            os.makedirs(f'C:/SVSHARE/MMEX_Populater/Selenium/Test-Population/{today}')
    finally:
        with open(f'C:/SVSHARE/MMEX_Populater/Selenium/Test-Population/{today}/{project}.txt', 'w+') as f:
            f.write(f"{url}")
        print(url)


func("ADL-S-PRQ")
func("ADL-P-PRQ")
func("ADL-S-BGA")
