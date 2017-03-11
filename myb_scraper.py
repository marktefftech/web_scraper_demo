import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException

# Initialize the Chrome driver
def init_driver():
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 5)
    return driver

# Standard function to request a web address from the initialized Chrome driver
def get_address(address):
    driver.get(address)

# Important function to get max on page
def get_max_on_page():
    # nav to max items allowed on page
    try:
        # Use xpath to find button to allow more items on the page
        binding_machines_max = driver.find_element_by_xpath("""/html/body/div[4]/div[2]
        /div[4]/div[2]/div/div/div/div[2]/div[2]/div/select""")
        # click the button
        binding_machines_max.click()
        # Use xpath to find the 6th and highest option for the most amount of items (on one page)
        max_list = driver.find_element_by_xpath("""/html/body/div[4]/div[2]/div[4]/div[2]/div/div/
        div/div[2]/div[2]/div/select/option[6]""")
        # Click on the 6th option
        max_list.click()
    except:
        print('Max allowed was indeed not allowed :(')
    else:
        # Allow wait time for JavaScript to load
        driver.implicitly_wait(10)
        time.sleep(1)

def print_list(category):
    # Get all of the equipment listed on page
    try:
        # Use class name to locate each listed item on page
        binding_items_list = driver.find_elements_by_class_name("row-10")
        # Open the csv file to start itemizing and adding to it
        with open('{}.csv'.format(category), 'w') as csvfile:
            fieldnames = ['Product_name', 'Price', ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        # Itemize the list for printing to the screen and to the csv file
        for idx, item in enumerate(binding_items_list):
            product_name = item.find_element_by_css_selector("h2.product-name")
            product_desc = item.find_element_by_css_selector("div.desc")
            product_price = item.find_element_by_css_selector("span.price")
            print("""

{} {}

Product info:
{}
{}
""".format(idx + 1, product_name.text, product_desc.text, product_price.text))
            # Add the list to the csv file
            with open('{}.csv'.format(category), 'a') as fp:
                wr = csv.writer(fp)
                wr.writerow([product_name.text, product_price.text])

    except:
        print('The function for printing and saving to csv failed... You failed :(')
    else:
        driver.implicitly_wait(10)

# This function traverses the dom to find each section and category. Then it s
def get_all_coil_machines():
    # nav to binding machines
    try:
        # wait until class is loaded
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'nav_binding_machines'))
        )
        # Use id to find the binding machines
        binding_machines = driver.find_element_by_id('nav_binding_machines')
        # Click on the binding machines option
        binding_machines.click()
    except:
        print('*The function to find and click the Binding Machines tab failed*')
    else:
        driver.implicitly_wait(10)

    #nav to selected binding machines
    try:
        # Use id to find the binding machines type
        binding_machines_coil = driver.find_element_by_id('machine-coil')
        # click the machine type
        binding_machines_coil.click()
    except:
        print('*The function to click on the Coil binding machines failed*')
    else:
        driver.implicitly_wait(10)

    # nav to the fist (from the left) category of type machine
    try:
        binding_machines_tile_left = driver.find_element_by_class_name("tile-left")
        binding_machines_tile_left.click()

    except:
        print('*The function to click on the Manual Coil binding machines failed*')
    else:
        driver.implicitly_wait(10)
        get_max_on_page()
        print_list("Manual Coil binding machines")
        driver.execute_script("window.history.go(-2)")
        time.sleep(1)

    # nav to the second (from the left) category of type machine
    try:
        binding_machines_tile_mid = driver.find_element_by_class_name("tile-mid")
        binding_machines_tile_mid.click()

    except:
        print('*The function to click on the Electric Coil binding machines failed*')
    else:
        driver.implicitly_wait(10)
        get_max_on_page()
        print_list("Electric Coil binding machines")
        driver.execute_script("window.history.go(-1)")
        time.sleep(1)

    # nav to the fourth tile-right (from the left) category of type machine
    try:
        binding_machines_tile_right = driver.find_element_by_class_name("tile-right")
        binding_machines_tile_right.click()

    except:
        print('*The function to click on the Inserters Coil binding machines failed*')
    else:
        driver.implicitly_wait(10)
        get_max_on_page()
        print_list("Inserters Coil binding machines")
        time.sleep(1)


if __name__ == "__main__":
    driver = init_driver()
    get_address("https://www.mybinding.com/")
    get_all_coil_machines()
    time.sleep(3)
    driver.quit()