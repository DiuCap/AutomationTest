from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

timeout = 15
def get_age(url):
	global timeout
	driver.get(url)
	name_present = EC.presence_of_element_located((By.CLASS_NAME, 'userName'))
	WebDriverWait(driver, timeout).until(name_present)
	user_element = driver.find_element_by_class_name('userName')
	# print("type user_element", type(user_element))
	span_element = user_element.find_elements_by_xpath('.//span')
	print('Age:', span_element[0].get_attribute('innerText'))

def site_login(url, username, password):
	global timeout
	driver.get (url)
	phone_present = EC.presence_of_element_located((By.NAME, 'phone'))
	WebDriverWait(driver, timeout).until(phone_present)

	phone_element = driver.find_element_by_name('phone')
	if not phone_element:
	    raise Exception("Cannot find phone elemenet. Abort")
        
    phone_element.send_keys(username)
    password_element = driver.find_element_by_name('password')
    if not password_element:
        raise Exception("Cannot find password elemenet. Abort")
        
    password_element.send_keys(password)
    driver.find_element_by_class_name('full-width').click()

    login_wait = WebDriverWait(driver, timeout)
    login_wait.until(lambda driver: driver.current_url != url)

    get_age('https://stage-www.keyflow.com/en/profile/me')

# credentials
username = '+46761177777'
password = 'testerQA123'
login_url = 'https://stage-www.keyflow.com/en/profile/login'
# initialize the Chrome driver
driver = webdriver.Chrome()
site_login(login_url, username, password)
