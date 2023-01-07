class Hotels:
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.select import Select
    from datetime import datetime
    import time
    

    place_input = input("Enter the City name: ")

    date_input =  input("Enter the check_in_date in format YYYY-MM-DD: ")

    parsed_date = datetime.strptime(date_input, '%Y-%M-%d')

    check_out_date_input = input("Enter the check out date in format YYYY-MM-DD: ")

    parsed_date2 = datetime.strptime(check_out_date_input, '%Y-%m-%d')

    adult = input("Enter total number of adults: ")
    
    childen = input("Enter total number of Children: ")

    values = input("Enter the values to be selected from the dropdowns, separated by commas: ").split(",")

    rooms = input("Enter the total number of rooms: ")

    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('https://www.booking.com')
    time.sleep(5)
    
    place = driver.find_element(By.XPATH, '//input[contains (@data-component, "search/destination/input-placeholder")]')
    place.click()
    place.send_keys(place_input)
    driver.find_element(By.XPATH, '//li[contains(@data-i,"0")]').click()
    time.sleep(2)
    
    ##date
    cal_btn = driver.find_element(By.XPATH, '//div[contains(@data-bui-ref,"calendar-next")]')
    month_name = driver.find_element(By.XPATH, '(//div[contains(@class,"bui-calendar__month")])[1]')

    if month_name.text != parsed_date.strftime("%B %Y"):
            cal_btn.click()
    
    time.sleep(5)

    date = driver.find_element(By.XPATH, f'(//td[contains(@data-date, "{parsed_date.strftime("%Y-%m-%d")}")])')
    date.click()
    time.sleep(2)

    return_date = driver.find_element(By.XPATH, f'(//td[contains(@data-date, "{parsed_date2.strftime("%Y-%m-%d")}")])')
    date.click()
    time.sleep(2)

    driver.find_element(By.XPATH,'(//label[contains(@id,"xp__guests__toggle")])').click()
    time.sleep(2)
    
    driver.find_element(By.XPATH, '(//div[contains(@class,"bui-stepper__wrapper sb-group__stepper-a11y")])[1]')
    inc_btn = driver.find_element(By.XPATH, '(//button[contains(@data-bui-ref, "input-stepper-add-button")])[1]')
    adult_text = driver.find_element(By.XPATH, '(//span[contains(@data-bui-ref,"input-stepper-value")])[1]')

    while adult_text.text != adult:
        inc_btn.click()

    time.sleep(2)

    driver.find_element(By.XPATH, '(//div[contains(@class,"bui-stepper__wrapper sb-group__stepper-a11y")])[2]')
    in_btn = driver.find_element(By.XPATH, '(//button[contains(@data-bui-ref, "input-stepper-add-button")])[2]')
    child_text = driver.find_element(By.XPATH, '(//span[contains(@data-bui-ref,"input-stepper-value")])[2]')

    while child_text.text != childen:
        in_btn.click()
    time.sleep(2)

    dropdowns = driver.find_elements(By.XPATH, '//select[contains(@name,"age")]')
    
    for dropdown, value in zip(dropdowns,values):
        select = Select(dropdown)
        select.select_by_value(value.strip())

    time.sleep(2)

    driver.find_element(By.XPATH, '(//div[contains(@class,"bui-stepper__wrapper sb-group__stepper-a11y")])[3]')
    incc_btn = driver.find_element(By.XPATH, '(//button[contains(@data-bui-ref, "input-stepper-add-button")])[3]')
    room_text = driver.find_element(By.XPATH, '(//span[contains(@data-bui-ref,"input-stepper-value")])[3]')

    while room_text.text != rooms:
        incc_btn.click()
    
    time.sleep(2)

    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    
    time.sleep(20)

    driver.quit()

   