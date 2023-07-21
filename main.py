from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd


navegador = webdriver.Edge()

dados = pd.read_excel("challenge.xlsx")


navegador.get("https://rpachallenge.com/")
sleep(10)

#### Butttons de start e submit
btn_start = navegador.find_element(By.XPATH, '//button[normalize-space()="Start"]')
btn_submit = navegador.find_element(By.XPATH, '//input[@value="Submit"]')


btn_start.click()

for index, row in dados.iterrows():

    ##### VALORES
    first_name = row['First Name']
    last_name = row['Last Name ']
    company_name = row['Company Name']
    role_in_company = row['Role in Company']
    address = row['Address']
    email = row['Email']
    phone_number = row['Phone Number']

    
    ### INPUTS
    input_first_name = navegador.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelFirstName"]').send_keys(first_name)
    input_last_name = navegador.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelLastName"]').send_keys(last_name)
    input_company_name = navegador.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelCompanyName"]').send_keys(company_name)
    input_role_in_company = navegador.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelRole"]').send_keys(role_in_company)
    input_address = navegador.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelAddress"]').send_keys(address)
    input_email = navegador.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelEmail"]').send_keys(email)
    input_phone_number = navegador.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelPhone"]').send_keys(phone_number)
    btn_submit.click()


sleep(10)