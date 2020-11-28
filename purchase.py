import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

def buy_product(username, password):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    url = 'https://www.walmart.com/ip/Sony-PlayStation-4-1TB-Slim-Gaming-Console/101507200'

    # Navigate to URL
    driver.get(url)

    # Click Add to Cart
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div[1]/section/div[1]/div[3]/button').click()
    
    # Sleep for 2 seconds (required for page to fully load)
    time.sleep(2)

    # Select Cart
    driver.find_element_by_xpath('/html/body/div/div/section[1]/div[2]/div/div[3]/div[2]/div/div[2]/div[3]').click()
    
    # Select Check out
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/button[1]').click()

    # Another unfortunate sleep
    time.sleep(1)

    # Input email address
    driver.find_element_by_xpath('//*[@id="sign-in-email"]').send_keys(username)
    
    # Input password
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[4]/div/section/div/section/form/div[2]/div/div[1]/label/div[2]/div/input').send_keys(password)

    # Uncheck Remember me
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[4]/div/section/div/section/form/div[4]/div').click()
    
    # Yep, another one or the CAPCHTA will get you
    time.sleep(2)

    # Click Submit
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[4]/div/section/div/section/form/div[5]/button').click()

    # Final Continue
    # driver.find_element_by_id('button').click()   # NEED to fix. Can't seem to get past this button. Need to take a breather.


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-u', '--username', help="Enter the username in SINGLE QUOTES, using the following format: 'username@mail.com' ")
    parser.add_argument('-p', '--password', help="Enter the password in SINGLE QUOTES, using the following format: 'g&ghs3k)!@(*7jh@KJhjkh8' ")

args = parser.parse_args()

buy_product(args.username, args.password)