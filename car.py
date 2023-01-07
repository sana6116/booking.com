from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from datetime import datetime

class Car:
    

    trip_trip = {
        "1" : "Return to same location",
        "2" : "Return to different location"
    }

    trip_trip_input = input("Enter the serial number for trip type you prefer: ")

    location_input = input("Enter the  full location: ")

    drop_up_location_input = input ("Enter your drop of location: ")

    date_input = input("Enter your trip date in format YYYY-MM-DD: ")

    to_date_input = input("Enter your return date YYYY-MM-DD: ")

    parsed_from_date = datetime.strptime(date_input, "%Y-%m-%d")
    parsed_to_date = datetime.strptime(to_date_input, "%Y-%m-%d")

    check_in_hour_input = input("Enter the hour of the check in: ")
    check_in_min_input = input("Enter the min(options: 00 or 15 or 30 or 45): ")

    check_out_hour_input = input("Enter the check out hour :")
    check_out_min_input = input("Enter the min (00 or 15 or 30 or 45):  ")



    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    driver.get('https://www.booking.com/cars')
    time.sleep(2)

    if trip_trip_input == "1":
        location = driver.find_element(By.XPATH, '//input[@data-component="search/destination/input-placeholder"]')
        location.click()
        location.send_keys(location_input)
        location.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="frm"]/div[2]/div[1]/div/div[1]/ul[1]/li').click()
        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="frm"]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div/button').click()
        time.sleep(5)

        #btn = driver.find_element(By.XPATH, "(//div[contains(@class,'sb-searchbox__input')])[1]/button")
        

        str1 = f"(//*[contains(@class,'c2-month-header-monthname')][contains(text(),'{parsed_from_date.strftime('%B %Y')}')])[1]/../../..//*[contains(@class,'c2-day')]/span[contains(text(),'{parsed_from_date.day}')]" 
        print(str1)
        from_date_button = driver.find_element(
            By.XPATH,
            str1
        )
        from_date_button.click()
        time.sleep(2)

        

        str2=f"(//*[contains(@class,'c2-month-header-monthname')][contains(text(),'{parsed_to_date.strftime('%B %Y')}')])[2]/../../..//*[contains(@class,'c2-day')]/span[contains(text(),'{parsed_to_date.day}')]"
        print(str2)

        to_date_button = driver.find_element(
            By.XPATH,
            str2
        )

        print(to_date_button)

        driver.execute_script("arguments[0].click()", to_date_button)
        time.sleep(5)

        driver.find_element(By.XPATH, '//*[@id="frm"]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div/button').click()
        time.sleep(5)

        check_in_hour = Select(driver.find_element(By.XPATH, '(//select[contains(@name, "checkinTime")])[1]'))
        check_in_hour.select_by_value(check_in_hour_input)
        time.sleep(2)

        check_in_min = Select(driver.find_element(By.XPATH, '(//select[contains(@name, "checkinTime")])[2]'))
        check_in_min.select_by_value(check_in_min_input)
        time.sleep(10)
        
        check_out_hour = Select(driver.find_element(By.XPATH, '(//select[contains(@name, "checkoutTime")])[1]'))
        check_out_hour.select_by_value(check_out_hour_input)
        time.sleep(10)

        check_out_min = Select(driver.find_element(By.XPATH, '(//select[contains(@name, "checkoutTime")])[2]'))
        check_out_min.select_by_value(check_out_min_input)
        time.sleep(10)

        driver.find_element(By.XPATH, '(//div[contains(@data-component, "search/dates/date-field-with-time")])[2]').click()
        time.sleep(5)

        driver.find_element(By.XPATH, '(//button[contains(@type, "submit")])').click()
        time.sleep(10)

    elif trip_trip_input == "2":
        driver.find_element(By.XPATH, '//label[@for="return-location-different"]').click()
        time.sleep(2)

        location = driver.find_element(By.XPATH, '//input[@data-component="search/destination/input-placeholder"]')
        location.click()
        location.send_keys(location_input)
        location.send_keys(Keys.ENTER)
        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="frm"]/div[2]/div[1]/div/div[1]/ul[1]/li').click()
        time.sleep(2)

        drop_up_location = driver.find_element(By.XPATH, '//input[contains(@placeholder, "Drop-off location")]')
        drop_up_location.click()
        drop_up_location.send_keys(drop_up_location_input)
        time.sleep(2)

        driver.find_element(By.XPATH, '(//ul[contains(@aria-label, "List of suggested destinations")])[2]//li[contains(@data-i, "1")]').click()
        
        driver.find_element(By.XPATH, '//*[@id="frm"]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div/button').click()
        time.sleep(5)

        #btn = driver.find_element(By.XPATH, "(//div[contains(@class,'sb-searchbox__input')])[1]/button")
        

        str1 = f"(//*[contains(@class,'c2-month-header-monthname')][contains(text(),'{parsed_from_date.strftime('%B %Y')}')])[1]/../../..//*[contains(@class,'c2-day')]/span[contains(text(),'{parsed_from_date.day}')]" 
        print(str1)
        from_date_button = driver.find_element(
            By.XPATH,
            str1
        )
        from_date_button.click()
        time.sleep(2)

        

        str2=f"(//*[contains(@class,'c2-month-header-monthname')][contains(text(),'{parsed_to_date.strftime('%B %Y')}')])[2]/../../..//*[contains(@class,'c2-day')]/span[contains(text(),'{parsed_to_date.day}')]"
        print(str2)

        to_date_button = driver.find_element(
            By.XPATH,
            str2
        )

        print(to_date_button)

        driver.execute_script("arguments[0].click()", to_date_button)
        time.sleep(5)

        driver.find_element(By.XPATH, '//*[@id="frm"]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div/button').click()
        time.sleep(5)

        check_in_hour = Select(driver.find_element(By.XPATH, '(//select[contains(@name, "checkinTime")])[1]'))
        check_in_hour.select_by_value(check_in_hour_input)
        time.sleep(2)

        check_in_sec = Select(driver.find_element(By.XPATH, '(//select[contains(@name, "checkinTime")])[2]'))
        check_in_sec.select_by_value(check_in_min_input)
        time.sleep(10)
        
        check_out_hour = Select(driver.find_element(By.XPATH, '(//select[contains(@name, "checkoutTime")])[1]'))
        check_out_hour.select_by_value(check_out_hour_input)
        time.sleep(10)

        check_out_min = Select(driver.find_element(By.XPATH, '(//select[contains(@name, "checkoutTime")])[2]'))
        check_out_min.select_by_value(check_out_min_input)
        time.sleep(10)

        driver.find_element(By.XPATH, '(//div[contains(@data-component, "search/dates/date-field-with-time")])[2]').click()
        time.sleep(5)

        driver.find_element(By.XPATH, '(//button[contains(@type, "submit")])').click()
        time.sleep(10)  

    else:
      print("Wrong input")
           
    time.sleep(10)
    driver.quit()