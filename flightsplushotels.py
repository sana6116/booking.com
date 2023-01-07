class FlightnHotels:
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from datetime import datetime
    import time

    trip_type = {
        "1" : "One-way",
        "2" : "Round-trip"
    }
    print(trip_type)
    trip_type_input = input("Enter the trip type number you wanna travel: ")


    class_type = [
        "Economy",
        "Premium economy",
        "Business",
        "First"
    ]
    print(class_type)
    class_type_input = input("Enter the class type: ").title()


    frm_input = input("Enter the place you want to fly from: ")

    to_input = input("Enter the place you want to fly to: ")

    date_input = input("Enter the date in fromat YYYY-MM-DD: ")

    parsed_date = datetime.strptime(date_input, "%Y-%m-%d")

    return_date_input = input("Enter return date in format YYYY-MM-DD: ")

    parsed_date_2 = datetime.strptime(return_date_input, "%Y-%m-%d" )

    adult_no = input("Enter the total number of adults: ")

    child_no = input("Enter the total number of children: ")

    infant_no = input("Enter the total number of infants: ")

    room_no = input("Enter the number of rooms: ")

    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    driver.get('https://www.agoda.com/c/booking')
    time.sleep(2)

    driver.find_element(By.XPATH, '(//button[contains(@data-element-name, "flight-cabin-class-button")])').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//span[contains(text(), "'+class_type_input+'")]').click()

    time.sleep(2)
    if trip_type_input == "1":
        driver.find_element(By.XPATH, '//button[contains(@data-element-name,"flight-option-button")]').click()
        time.sleep(5)

        driver.find_element(By.XPATH, '//span[contains(@class, "Spanstyled__SpanStyled-sc-16tp9kb-0 gwICfd kite-js-Span ")][1]').click()
        time.sleep(2)
   
        fly_from = driver.find_element(By.XPATH, '//input[contains(@aria-label,"Flying from")]')
        fly_from.click()
        fly_from.send_keys(frm_input)
        time.sleep(2)
        driver.find_element(By.XPATH, ' //ul[contains(@class, "AutocompleteList AutocompleteSearch__AutocompleteList" )]//li[1]').click()
        time.sleep(2)

        fly_to = driver.find_element(By.XPATH, '//input[contains(@aria-label, "Flying to")]')
        fly_to.click()
        fly_to.send_keys(to_input)
        time.sleep(2)
        driver.find_element(By.XPATH, ' //ul[contains(@class, "AutocompleteList AutocompleteSearch__AutocompleteList" )]//li[1]').click()
        time.sleep(2)

        #date
        nxt_btn = driver.find_element(By.XPATH, '//span[contains(@aria-label,"Next Month")]')

        month_year = driver.find_elements(By.XPATH, '//div[contains(@class,"DayPicker-Caption")]/div[1]')

        for m_y in month_year:
            if m_y.text != parsed_date.strftime("%m %Y"):
                nxt_btn.click()
        time.sleep(2)
        date = driver.find_element(By.XPATH, '//span[contains(text(), "'+parsed_date.strftime("%d")+'")]')
        date.click()
        time.sleep(2)

        #adult passengers

        ap_btn = driver.find_element(By.XPATH, '(//span[contains(@data-element-name,"flight-occupancy-adult-increase")])')
        a_text = driver.find_element(By.XPATH, '(//span[contains(@data-component, "flight-occupancy-adult-number")])')

        while a_text.text != adult_no:
            ap_btn.click()
        
        time.sleep(2)

        #child passengers

        cp_btn = driver.find_element(By.XPATH, '(//span[contains(@data-element-name,"flight-occupancy-children-increase")])')
        c_text = driver.find_element(By.XPATH, '(//span[contains(@data-component, "flight-occupancy-children-number")])')

        while c_text.text != child_no:
            cp_btn.click()

        time.sleep(2)

        #infant

        ip_btn = driver.find_element(By.XPATH, '(//span[contains(@data-element-name,"flight-occupancy-infant-increase")])')
        i_text = driver.find_element(By.XPATH, '(//span[contains(@data-component, "flight-occupancy-infant-number")])')

        while i_text.text != infant_no:
            ip_btn.click()

        time.sleep(2)


        driver.find_element(By.XPATH, '(//span[contains(@class, "Spanstyled__SpanStyled-sc-16tp9kb-0 ecwFCQ kite-js-Span Box-sc-kv6pi1-0 jJvGxG")])').click()
        time.sleep(2)

        #rooms
        driver.find_element(By.XPATH, f'(//div[contains(@data-selenium,"room-option-{room_no}")])').click()
        time.sleep(2)

        driver.find_element(By.XPATH, '(//button[contains(@data-component,"flight-search-button")])').click()
        time.sleep(20)

    if trip_type_input == "2":
        driver.find_element(By.XPATH, '//button[contains(@data-element-name,"flight-option-button")]').click()
        time.sleep(5)

        driver.find_element(By.XPATH, '(//div[contains(@data-element-object-id,"round-trip")])').click()
        time.sleep(2)
   
        fly_from = driver.find_element(By.XPATH, '//input[contains(@aria-label,"Flying from")]')
        fly_from.click()
        fly_from.send_keys(frm_input)
        time.sleep(2)
        driver.find_element(By.XPATH, ' //ul[contains(@class, "AutocompleteList AutocompleteSearch__AutocompleteList" )]//li[1]').click()
        time.sleep(2)

        fly_to = driver.find_element(By.XPATH, '//input[contains(@aria-label, "Flying to")]')
        fly_to.click()
        fly_to.send_keys(to_input)
        time.sleep(2)
        driver.find_element(By.XPATH, ' //ul[contains(@class, "AutocompleteList AutocompleteSearch__AutocompleteList" )]//li[1]').click()
        time.sleep(2)

        #date
        nxt_btn = driver.find_element(By.XPATH, '//span[contains(@aria-label,"Next Month")]')

        month_year = driver.find_elements(By.XPATH, '//div[contains(@class,"DayPicker-Caption")]/div[1]')

        for m_y in month_year:
            if m_y.text != parsed_date.strftime("%m %Y"):
                nxt_btn.click()
        time.sleep(2)
        date = driver.find_element(By.XPATH, '//span[contains(text(), "'+parsed_date.strftime("%d")+'")]')
        date.click()
        time.sleep(2)

        return_date = driver.find_element(By.XPATH, '//span[contains(text(), "'+parsed_date_2.strftime("%d")+'")]')
        return_date.click()
        time.sleep(2)

        #adult passengers

        ap_btn = driver.find_element(By.XPATH, '(//span[contains(@data-element-name,"flight-occupancy-adult-increase")])')
        a_text = driver.find_element(By.XPATH, '(//span[contains(@data-component, "flight-occupancy-adult-number")])')

        while a_text.text != adult_no:
            ap_btn.click()
        
        time.sleep(2)

        #child passengers

        cp_btn = driver.find_element(By.XPATH, '(//span[contains(@data-element-name,"flight-occupancy-children-increase")])')
        c_text = driver.find_element(By.XPATH, '(//span[contains(@data-component, "flight-occupancy-children-number")])')

        while c_text.text != child_no:
            cp_btn.click()

        time.sleep(2)

        #infant

        ip_btn = driver.find_element(By.XPATH, '(//span[contains(@data-element-name,"flight-occupancy-infant-increase")])')
        i_text = driver.find_element(By.XPATH, '(//span[contains(@data-component, "flight-occupancy-infant-number")])')

        while i_text.text != infant_no:
            ip_btn.click()

        time.sleep(2)


        driver.find_element(By.XPATH, '(//span[contains(@class, "Spanstyled__SpanStyled-sc-16tp9kb-0 ecwFCQ kite-js-Span Box-sc-kv6pi1-0 jJvGxG")])').click()
        time.sleep(2)

        #rooms
        driver.find_element(By.XPATH, f'(//div[contains(@data-selenium,"room-option-{room_no}")])').click()
        time.sleep(2)

        driver.find_element(By.XPATH, '(//button[contains(@data-component,"flight-search-button")])').click()
        time.sleep(20)
    
    else:
      print("Wrong input")
      
    time.sleep(20)
    driver.quit()