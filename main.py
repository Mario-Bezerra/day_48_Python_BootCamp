from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_drive_path = "C:\\Users\\Pichau\\Desktop\\JAVASCRIPT\\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_drive_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fn = driver.find_element(By.NAME, "fName")
ln = driver.find_element(By.NAME, "lName")
em = driver.find_element(By.NAME, "email")
fn.send_keys("Mario")
ln.send_keys("Bezerra")
em.send_keys("gabriel_bzr@hotmail.com")
em.send_keys(Keys.ENTER)