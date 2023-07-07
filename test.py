from selenium import webdriver
import openpyxl
from openpyxl import
import time

# Load Excel data

# Open the web page
driver = webdriver.Chrome()  # Change to the appropriate web driver if needed
driver.get('site login')  # Replace with the URL of the website you want to login to

# Find the login form elements and fill in the credentials
username_input = driver.find_element('id','email')
password_input = driver.find_element('id','password')
submit_button = driver.find_element('id','login')

username_input.send_keys('username')  # Replace with your actual username
password_input.send_keys('password')  # Replace with your actual password
submit_button.click()



driver.get('page to insert data url')

# Find form elements and fill them with Excel data
name_input = driver.find_element_by_id('name')
category_id_input = driver.find_element_by_id('category_id')
phone_input = driver.find_element_by_id('phone_no')
email_input = driver.find_element_by_id('email')
designation_input = driver.find_element_by_id('designation')
gender_input = driver.find_element_by_id('gender')
display_input = driver.find_element_by_id('display_order')

for row in sheet.iter_rows(min_row=2):  # Assuming data starts from the second row
    name = row[0].value
    category_id = row[1].value
    phone = row[2].value
    email = row[3].value
    designation = row[4].value
    gender = row[5].value
    dispaly_order = row[6].value
    

    name_input.send_keys(name)
    category_id_input.send_keys(category_id)
    phone_input.send_keys(phone)
    email_input.send_keys(email)
    designation_input.send_keys(designation)
    gender_input.send_keys(gender)
    display_order_input.send_keys(dispaly_order)

    # Submit the form (if necessary)
    submit_button = driver.find_element_by_id('submit-button-id')
    submit_button.click()

    # Clear the form fields for the next entry
    name_input.clear()
    category_id_input.clear()
    phone_input.clear()
    email_input.clear()
    designation_input.clear()
    gender_input.clear()
    display_order_input.clear()

# Close the browser
driver.quit()
