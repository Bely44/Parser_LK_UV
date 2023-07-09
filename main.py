import time

import openpyxl
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def lk_uv_parser():

    url = 'https://lkuv.gosuslugi.ru/paip-portal/#/exchange-session/v2'

    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(20)
    driver.get(url)
    input_id = driver.find_element(By.XPATH,
                                   '/html/body/app-root/div/exchange-session-v2-wizard/paip-screen-container/div/div/div[2]/div[2]/exchange-session-v2-set-message-id/div[1]/lib-standard-input/div/div/div[1]/input')
    input_id.send_keys('fea2d456-ce21-11ed-a887-0242ac110003')
    button = driver.find_element(By.XPATH,
                                      '/html/body/app-root/div/exchange-session-v2-wizard/paip-screen-container/div/div/div[2]/div[2]/exchange-session-v2-set-message-id/div[2]/lib-button/div/button')
    button.send_keys(Keys.ENTER)
    status = driver.find_element(By.XPATH,
                                 '/html/body/app-root/div/exchange-session-v2-wizard/paip-screen-container/div/div/div[2]/div[2]/exchange-session-v2-report/paip-tabs-container/div[3]/div/div/div[2]/div/div[1]/div[4]/p[2]')
    print(status.text)
    system = driver.find_element(By.XPATH,
                                 '/html/body/app-root/div/exchange-session-v2-wizard/paip-screen-container/div/div/div[2]/div[2]/exchange-session-v2-report/paip-tabs-container/div[3]/div/div/div[2]/div/div[1]/div[2]/a')
    print(system.text)
    kind_of_information = driver.find_element(By.XPATH,
                                              '/html/body/app-root/div/exchange-session-v2-wizard/paip-screen-container/div/div/div[2]/div[2]/exchange-session-v2-report/paip-tabs-container/div[3]/div/div/div[2]/div/div[1]/div[3]/p[2]')
    print(kind_of_information.text)
    request_date_time = driver.find_element(By.XPATH,
                                            '/html/body/app-root/div/exchange-session-v2-wizard/paip-screen-container/div/div/div[2]/div[2]/exchange-session-v2-report/paip-tabs-container/div[3]/div/div/div[1]/paip-nested-stepper[1]/paip-nested-stepper-item/paip-nested-stepper-item[3]/div/div[2]/div/p')
    print(request_date_time.text)
    response_name = driver.find_element(By.XPATH,
                                        '/html/body/app-root/div/exchange-session-v2-wizard/paip-screen-container/div/div/div[2]/div[2]/exchange-session-v2-report/paip-tabs-container/div[3]/div/div/div[2]/div/div[2]/div[1]/a')
    print(response_name.text)
    duration_value = driver.find_element(By.XPATH,
                                         '/html/body/app-root/div/exchange-session-v2-wizard/paip-screen-container/div/div/div[2]/div[2]/exchange-session-v2-report/paip-tabs-container/div[3]/div/div/div[2]/div/div[2]/div[3]/p[2]')
    print(duration_value.text)
    respondent_smev = driver.find_element(By.XPATH,
                                          '/html/body/app-root/div/exchange-session-v2-wizard/paip-screen-container/div/div/div[2]/div[2]/exchange-session-v2-report/paip-tabs-container/div[3]/div/div/div[1]/paip-nested-stepper[2]/paip-nested-stepper-item/paip-nested-stepper-item[4]/div/div[2]/div/p')
    print(respondent_smev.text)
    queued_date_time = driver.find_element(By.XPATH,
                                 '/html/body/app-root/div/exchange-session-v2-wizard/paip-screen-container/div/div/div[2]/div[2]/exchange-session-v2-report/paip-tabs-container/div[3]/div/div/div[1]/paip-nested-stepper[2]/paip-nested-stepper-item/paip-nested-stepper-item[4]/div/div[2]/div/p')
    print(queued_date_time.text)
    pull_date_time = driver.find_element(By.XPATH,
                                         '/html/body/app-root/div/exchange-session-v2-wizard/paip-screen-container/div/div/div[2]/div[2]/exchange-session-v2-report/paip-tabs-container/div[3]/div/div/div[1]/paip-nested-stepper[2]/paip-nested-stepper-item/paip-nested-stepper-item[2]/div/div[2]/div/p')
    print(pull_date_time.text)
    ack_date_time = driver.find_element(By.XPATH,
                                        '/html/body/app-root/div/exchange-session-v2-wizard/paip-screen-container/div/div/div[2]/div[2]/exchange-session-v2-report/paip-tabs-container/div[3]/div/div/div[1]/paip-nested-stepper[2]/paip-nested-stepper-item/paip-nested-stepper-item[3]/div/div[2]/div/p')
    print(ack_date_time.text)


lk_uv_parser()

