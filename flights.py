class Flights:
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.select import Select
    from datetime import datetime
    import time
    
    trip_type = {
       "1" : "Round Trip",
       "2" : "One-Way Trip",
       "3" : "Multi-City Trip"
    }
    print(trip_type)
    choose = input("Choose your trip type from the list: ")
    
    
    class_type = {
        "Economy",
        "Premium_economy", 
        "Business", 
        "First-class"
    }
    print(class_type)
    choose_class_type = input("Enter the class_type you wanna travel in: ").upper()

    adult_input = input("Enter the total number of adults: ")

    children = input("Enter the total number of children: ")

    kids_ages = input("Enter the values to be selected from the dropdowns, separated by commas: ").split(",")

    where_input = input("Enter the the place you wanna fly from: ")

    to_input = input("Enter the the place you wanna fly to: ")

    where2_input = input("Enter the the place you wanna fly from(only for multiple city travel): ")

    to2_input = input("Enter the the place you wanna fly to(only for multiple city travel): ")

    date = input("Enter the date of your trip in format YYYY-MM-DD: ")
    
    return_date = input("Enter the date of return from trip in format YYYY-MM-DD: ")

    parsed_date = datetime.strptime(date, "%Y-%m-%d")

    parsed_date_2 = datetime.strptime(return_date, "%Y-%m-%d")

    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    driver.get('https://www.booking.com/flights')
    time.sleep(2)

    class_type = Select(driver.find_element(By.XPATH, '//select[contains(@class,"css-1k0jlfl")]'))
    class_type.select_by_value(choose_class_type)
    time.sleep(2)
    ## passengers:

    driver.find_element(By.XPATH, '//div[contains(@data-testid,"input_occupancy_desktop_passengers_trigger")]').click()
    time.sleep(2)
    
    driver.find_element(By.XPATH, '(//div[contains(@class,"css-qx6f9e")])[1]')
    adult_text = driver.find_element(By.XPATH, '(//div[contains(@class,"css-1spspr5")])[1]')
    adult_btn = driver.find_element(By.XPATH, '(//button[contains(@data-testid,"input_occupancy_modal_adults_increase")])')

    while adult_text.text != adult_input:
        adult_btn.click()

    time.sleep(2)

    driver.find_element(By.XPATH, '(//div[contains(@class,"css-qx6f9e")])[2]')
    adult_text = driver.find_element(By.XPATH, '(//div[contains(@class,"css-1spspr5")])[2]')
    adult_btn = driver.find_element(By.XPATH, '(//button[contains(@data-testid,"input_occupancy_modal_children_increase")])')

    while adult_text.text != adult_input:
        adult_btn.click()

    time.sleep(2)

    dropdowns = driver.find_elements(By.XPATH, '(//select[contains(@name,"children")])')

    for dropdown, kids_age in zip(dropdowns, kids_ages):
        select = Select(dropdown)

        select.select_by_visible_text(kids_age.strip())

    time.sleep(2)

    driver.find_element(By.XPATH, '//button[contains(@data-testid,"input_occupancy_desktop_done")]').click()

    time.sleep(2)

    if choose == "1":
        driver.find_element(By.XPATH, '//span[contains(@class, "InputRadio-module__field___4Jbyo")][1]').click()
        time.sleep(2)

        driver.find_element(By.XPATH, '//div[contains(@class, "css-g1y0tj-inputContainer")]').click()
        time.sleep(2)
        where = driver.find_element(By.XPATH, '//input[contains(@data-testid, "searchbox_origin_input_0")]')
        where.click()
        where.send_keys(Keys.BACK_SPACE)
        where.send_keys(where_input)
        time.sleep(5)
        driver.find_element(By.XPATH, '//li[contains(@data-sr-autocomplete-li,"0")]').click()
        time.sleep(5)

        to = driver.find_element(By.XPATH, '(//input[contains(@data-testid,"searchbox_destination_input_0")])')
        to.click()
        to.send_keys(to_input)
        time.sleep(5)
        driver.find_element(By.XPATH, '//li[contains(@data-sr-autocomplete-li,"0")]').click()
        time.sleep(5)

        #date
        driver.find_element(By.XPATH, '(//input[contains(@placeholder, "Depart")])').click()
        time.sleep(2)
        inc_btn = driver.find_element(By.XPATH, '(//div[contains(@class, "Calendar-module__root___-ToJj")]//button)[2]')
        month_names = driver.find_elements(By.XPATH, '(//div[contains(@class, "Calendar-module__monthWrapper___K2bU1")]//h3)[1]')

        for name in month_names:
            if name.text != parsed_date.strftime("%m %d"):
                inc_btn.click()
        time.sleep(2)

        date = driver.find_element(By.XPATH, f'(//span[contains(@data-date,"{parsed_date.strftime("%Y-%m-%d")}")])')
        date.click()
        time.sleep(10)

        date_2 = driver.find_element(By.XPATH, f'(//span[contains(@data-date,"{parsed_date_2.strftime("%Y-%m-%d")}")])')
        date_2.click()
        time.sleep(10)
        
        driver.find_element(By.XPATH, '//button[contains(@data-testid,"searchbox_submit")]').click()
        time.sleep(2)
    
    elif choose == "2":
        driver.find_element(By.XPATH, '(//label[contains(@class,"InputRadio-module__container___IUNVN")])[2]').click()
        time.sleep(2)
        
        driver.find_element(By.XPATH, '//div[contains(@class, "css-g1y0tj-inputContainer")]').click()
        time.sleep(2)
        where = driver.find_element(By.XPATH, '//input[contains(@data-testid, "searchbox_origin_input_0")]')
        where.click()
        where.send_keys(Keys.BACK_SPACE)
        where.send_keys(where_input)
        time.sleep(5)
        driver.find_element(By.XPATH, '//li[contains(@data-sr-autocomplete-li,"0")]').click()
        time.sleep(5)

        to = driver.find_element(By.XPATH, '(//input[contains(@data-testid,"searchbox_destination_input_0")])')
        to.click()
        to.send_keys(to_input)
        time.sleep(5)
        driver.find_element(By.XPATH, '//li[contains(@data-sr-autocomplete-li,"0")]').click()
        time.sleep(5)

        #date
        driver.find_element(By.XPATH, '(//input[contains(@placeholder, "Depart")])').click()
        time.sleep(2)
        inc_btn = driver.find_element(By.XPATH, '(//div[contains(@class, "Calendar-module__root___-ToJj")]//button)[2]')
        month_names = driver.find_elements(By.XPATH, '(//div[contains(@class, "Calendar-module__monthWrapper___K2bU1")]//h3)[1]')

        for name in month_names:
            if name.text != parsed_date.strftime("%m %d"):
                inc_btn.click()
        time.sleep(2)

        date = driver.find_element(By.XPATH, f'(//span[contains(@data-date,"{parsed_date.strftime("%Y-%m-%d")}")])')
        date.click()
        time.sleep(10)

        driver.find_element(By.XPATH, '//button[contains(@data-testid,"searchbox_submit")]').click()
        time.sleep(2)

    elif choose == "3":
        driver.find_element(By.XPATH, '(//label[contains(@class,"InputRadio-module__container___IUNVN")])[3]').click()
        time.sleep(2)
        
        driver.find_element(By.XPATH, '//div[contains(@class, "css-g1y0tj-inputContainer")]').click()
        time.sleep(2)
        where = driver.find_element(By.XPATH, '//input[contains(@data-testid, "searchbox_origin_input_0")]')
        where.click()
        where.send_keys(Keys.BACK_SPACE)
        where.send_keys(where_input)
        time.sleep(5)
        driver.find_element(By.XPATH, '//li[contains(@data-sr-autocomplete-li,"0")]').click()
        time.sleep(5)

        to = driver.find_element(By.XPATH, '(//input[contains(@data-testid,"searchbox_destination_input_0")])')
        to.click()
        to.send_keys(to_input)
        time.sleep(5)
        driver.find_element(By.XPATH, '//li[contains(@data-sr-autocomplete-li,"0")]').click()
        time.sleep(5)

        #date
        driver.find_element(By.XPATH, '(//input[contains(@placeholder, "Depart")])').click()
        time.sleep(2)
        inc_btn = driver.find_element(By.XPATH, '(//div[contains(@class, "Calendar-module__root___-ToJj")]//button)[2]')
        month_names = driver.find_elements(By.XPATH, '(//div[contains(@class, "Calendar-module__monthWrapper___K2bU1")]//h3)[1]')

        for name in month_names:
            if name.text != parsed_date.strftime("%m %d"):
                inc_btn.click()
        time.sleep(2)

        date = driver.find_element(By.XPATH, f'(//span[contains(@data-date,"{parsed_date.strftime("%Y-%m-%d")}")])')
        date.click()
        time.sleep(10)
        
        driver.find_element(By.XPATH, '(//input[contains(@placeholder,"Where from?")])[1]').click()
        time.sleep(2)
        where_2 = driver.find_element(By.XPATH, '(//input[contains(@data-testid,"searchbox_origin_input_1")])')
        where_2.click()
        where_2.send_keys(where2_input)
        time.sleep(5)
        driver.find_element(By.XPATH, '(//div[contains(@class,"css-5vmqig")])').click()
        time.sleep(2)

        to_2 = driver.find_element(By.XPATH, '(//input[contains(@data-testid,"searchbox_destination_input_1")])')
        to_2.click()
        to_2.send_keys(to2_input)
        time.sleep(5)
        driver.find_element(By.XPATH, '//div[contains(@class, "css-5vmqig")]').click()
        time.sleep(2)
    
        date_2 = driver.find_element(By.XPATH, f'//span[contains(@data-date,"{parsed_date_2.strftime("%Y-%m-%d")}")]')
        date_2.click()
        time.sleep(5)

        driver.find_element(By.XPATH, '//button[contains(@data-testid,"searchbox_submit")]').click()
        time.sleep(2)
    
    else:
      print("Wrong input")

    time.sleep(20)
    driver.quit()
   