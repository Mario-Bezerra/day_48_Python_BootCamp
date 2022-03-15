from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_drive_path = "C:\\Users\\Pichau\\Desktop\\JAVASCRIPT\\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_drive_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
game_on = True
big_cookie = driver.find_element(By.ID, "cookie")

time_end = time.time() + (60 * 5)

while True:

    if time.time() < time_end:

        t_end_ = time.time() + 7.5

        while time.time() < t_end_:

            cookie = driver.find_element(By.ID, 'cookie').click()

            if time.time() > t_end_:

                if int((driver.find_element(By.ID, 'money').text).replace(',', "")) > int(((
                (driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b')).text).split('-')[1].strip()).replace(
                        ',', "")):
                    driver.find_element(By.ID, "buyTime machine").click()

                elif int((driver.find_element(By.ID, 'money').text).replace(',', "")) > int(
                        (((driver.find_element(By.CSS_SELECTOR, "#buyPortal b")).text).split('-')[1].strip()).replace(
                                ',', "")):
                    driver.find_element(By.ID, "buyPortal").click()

                elif int((driver.find_element(By.ID, 'money').text).replace(',', "")) > int(((
                (driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b')).text).split('-')[1].strip()).replace(',',
                                                                                                                    "")):
                    driver.find_element(By.ID, "buyAlchemy lab").click()

                elif int((driver.find_element(By.ID, 'money').text).replace(',', "")) > int(
                        (((driver.find_element(By.CSS_SELECTOR, "#buyShipment b")).text).split('-')[1].strip()).replace(
                                ',', "")):
                    driver.find_element(By.ID, "buyShipment").click()

                elif int((driver.find_element(By.ID, 'money').text).replace(',', "")) > int(
                        (((driver.find_element(By.CSS_SELECTOR, "#buyMine b")).text).split('-')[1].strip()).replace(',',
                                                                                                                    "")):
                    driver.find_element(By.ID, "buyMine").click()

                elif int((driver.find_element(By.ID, 'money').text).replace(',', "")) > int(
                        (((driver.find_element(By.CSS_SELECTOR, "#buyFactory b")).text).split('-')[1].strip()).replace(
                                ',', "")):
                    driver.find_element(By.ID, "buyFactory").click()

                elif int((driver.find_element(By.ID, 'money').text).replace(',', "")) > int(
                        (((driver.find_element(By.CSS_SELECTOR, "#buyGrandma b")).text).split('-')[1].strip()).replace(
                                ',', "")):
                    driver.find_element(By.ID, "buyGrandma").click()

                elif int((driver.find_element(By.ID, 'money').text).replace(',', "")) > int(
                        (((driver.find_element(By.CSS_SELECTOR, "#buyCursor b")).text).split('-')[1].strip()).replace(
                                ',', "")):
                    driver.find_element(By.ID, "buyCursor").click()

    else:
        print(driver.find_element(By.ID, "cps").text)
        driver.quit()
        break