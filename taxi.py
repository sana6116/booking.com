class Taxi:
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.select import Select
    from datetime import datetime, date
    import time

    trip_type = {
        "1" : "One-Way",
        "2" : "round"
    }

    trip_type_input = input("Enter the key of the type of trip from the list: ")

    pick_up_location_input = input("Enter the pick up location: ")

    drop_off_input = input("Enter the drop off location: ")

    date_input = input("Enter your date in format YYYY-MM_DD: ")

    parsed_date = datetime.strptime(date_input, "%Y-%m-%d")

    return_date_input = input("Enter your return date in format YYYY-MM_DD: ") 

    parsed_date_2 = datetime.strptime(return_date_input, "%Y-%m-%d")

    pick_up_time_input = input("Enter the of pick up time in formant HH:MM: ")

    parsed_time = datetime.strptime(pick_up_time_input, "%H:%M")

    return_time = input("Enter the time to return in format HH:MM: ")

    parsed_time_2 = datetime.strptime(return_time, "%H:%M")

    passengers_input = input("Enter the number of passengers: ")
    
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('https://www.booking.com/taxi')
    time.sleep(5)

    if trip_type_input == "1":
        pick_up_location = driver.find_element(By.XPATH, '//input[contains(@id, "pickupLocation")]')
        pick_up_location.click()
        pick_up_location.send_keys(pick_up_location_input)
        pick_up_location.send_keys(Keys.ENTER)
        time.sleep(3)

        destination = driver.find_element(By.XPATH, '//input[contains(@id, "dropoffLocation")]')
        destination.click()
        destination.send_keys(drop_off_input)
        destination.send_keys(Keys.ENTER)
        time.sleep(3)

        driver.find_element(By.XPATH, '//button[contains(@aria-label,"pickup date input field")]').click()
        time.sleep(2)

        btn = driver.find_element(By.XPATH, '//button[contains(@data-test, "rw-date-picker__btn--next")]')
        time.sleep(2)
        month = driver.find_element(By.XPATH, '//table[contains(@class, "rw-c-date-picker__calendar ")]/caption[contains(@class, "rw-c-date-picker__calendar-caption")]')
        
        while month.text != parsed_date.strftime('%B %Y'):
                btn.click()

        time.sleep(2)
        string = f"//a[contains(@aria-label, '{parsed_date.strftime('%d, %B %Y')}')]"
        date1 = driver.find_element(By.XPATH, string)
        date1.click()
        time.sleep(5)

        driver.find_element(By.XPATH, '//button[contains(@aria-label, "pickup time input field")]').click()
        pick_up_hour = Select(driver.find_element(By.XPATH, '//select[contains(@id, "pickupHour")]'))
        pick_up_hour.select_by_value(parsed_time.strftime('%H'))
        time.sleep(2)

        pick_up_min = Select(driver.find_element(By.XPATH, '//select[contains(@id, "pickupMinute")]'))
        pick_up_min.select_by_value(parsed_time.strftime('%M'))
        time.sleep(2)

        driver.find_element(By.XPATH, '//button[contains(@data-test,"rw-time-picker__confirm-button")]').click()
        time.sleep(2)
        
        passengers = Select(driver.find_element(By.XPATH, '//select[contains(@id, "passengers")]'))
        passengers.select_by_value(passengers_input)
        time.sleep(4)

        driver.find_element(By.XPATH, '(//span[contains(@data-test,"button-content")])').click()
        time.sleep(2)

    elif trip_type_input == "2":
        driver.find_element(By.XPATH, '//span[contains(@data-test, "returnJourneyAffirmative-label")]').click()
        time.sleep(2)

        pick_up_location = driver.find_element(By.XPATH, '//input[contains(@id, "pickupLocation")]')
        pick_up_location.click()
        pick_up_location.send_keys(pick_up_location_input)
        pick_up_location.send_keys(Keys.ENTER)
        time.sleep(3)

        destination = driver.find_element(By.XPATH, '//input[contains(@id, "dropoffLocation")]')
        destination.click()
        destination.send_keys(drop_off_input)
        destination.send_keys(Keys.ENTER)
        time.sleep(3)

        driver.find_element(By.XPATH, '//button[contains(@aria-label,"pickup date input field")]').click()
        time.sleep(2)

        btn = driver.find_element(By.XPATH, '//button[contains(@data-test, "rw-date-picker__btn--next")]')
        time.sleep(2)
        month = driver.find_element(By.XPATH, '//table[contains(@class, "rw-c-date-picker__calendar ")]/caption[contains(@class, "rw-c-date-picker__calendar-caption")]')
        
        while month.text != parsed_date.strftime('%B %Y'):
                btn.click()

        time.sleep(2)
        string = f"//a[contains(@aria-label, '{parsed_date.strftime('%d, %B %Y')}')]"
        date1 = driver.find_element(By.XPATH, string)
        date1.click()
        time.sleep(5)

        driver.find_element(By.XPATH, '//button[contains(@aria-label, "pickup time input field")]').click()
        pick_up_hour = Select(driver.find_element(By.XPATH, '//select[contains(@id, "pickupHour")]'))
        pick_up_hour.select_by_value(parsed_time.strftime('%H'))
        time.sleep(2)

        pick_up_min = Select(driver.find_element(By.XPATH, '//select[contains(@id, "pickupMinute")]'))
        pick_up_min.select_by_value(parsed_time.strftime('%M'))
        time.sleep(2)

        driver.find_element(By.XPATH, '//button[contains(@data-test,"rw-time-picker__confirm-button")]').click() 
        passengers = Select(driver.find_element(By.XPATH, '//select[contains(@id, "passengers")]'))
        passengers.select_by_value(passengers_input)
        time.sleep(4)

        driver.find_element(By.XPATH, '//button[contains(@aria-label, "return date input field")]').click()
        time.sleep(2)

        btn = driver.find_element(By.XPATH, '//button[contains(@data-test, "rw-date-picker__btn--next")]')
        time.sleep(2)
        month = driver.find_element(By.XPATH, '//table[contains(@class, "rw-c-date-picker__calendar ")]/caption[contains(@class, "rw-c-date-picker__calendar-caption")]')
        
        while month.text != parsed_date_2.strftime('%B %Y'):
                btn.click()

        time.sleep(2)
        string = f"//a[contains(@aria-label, '{parsed_date_2.strftime('%d, %B %Y')}')]"
        date2 = driver.find_element(By.XPATH, string)
        date2.click()
        time.sleep(5)

        driver.find_element(By.XPATH, '//button[contains(@aria-label,"return time input field")]').click()

        pick_up_hour2 = Select(driver.find_element(By.XPATH, '//select[contains(@id, "returnHour")]'))
        pick_up_hour2.select_by_value(parsed_time_2.strftime('%H'))
        time.sleep(2)

        pick_up_min2 = Select(driver.find_element(By.XPATH, '//select[contains(@id, "returnMinute")]'))
        pick_up_min2.select_by_value(parsed_time_2.strftime('%M'))
        time.sleep(2)

        driver.find_element(By.XPATH, '//button[contains(@name,"searchButton")]').click()
        
    else:
      print("Wrong input")

       
        

    
    time.sleep(10)
    driver.quit()
