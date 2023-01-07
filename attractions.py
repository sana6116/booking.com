class Attractions:
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.select import Select
    from datetime import datetime
    import time

    where_input = input("Enter the place name: ")

    date = input("Enter the date in format YYYY-MM-DD: ")

    parsed_date = datetime.strptime(date, "%Y-%m-%d")
    
    date2 = input("Enter the date in format YYYY-MM-DD: ")

    parsed2_date = datetime.strptime(date2, "%Y-%m-%d")
    
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('https://www.booking.com/attractions')
    time.sleep(5)

    where = driver.find_element(By.XPATH, '//input[@name="query"]')
    where.click()
    where.send_keys(where_input)
    where.send_keys(Keys.ENTER)
    time.sleep(2)

    driver.find_element(By.XPATH, '//div[contains(@class, "css-17mdy6j")]').click()
    time.sleep(2)
    inc_btn = driver.find_element(By.XPATH, '(//div[contains(@class,"c5d667353d")]/button)')
    month_input = driver.find_elements(By.XPATH, '(//h3[contains(@class, "ac78a73c96 ab0d1629e5")])[1]')
    
    for month in month_input:
        if month.text != parsed_date.strftime("%m %Y"):
            inc_btn.click()
        inc_btn.click()
    time.sleep(5)

    date_input = driver.find_element(By.XPATH, '//span[contains(text(), "'+parsed_date.strftime("%d")+'")]')
    
    date_input.click()

    date2_input = driver.find_element(By.XPATH, '//span[contains(text(), "'+parsed2_date.strftime("%d")+'")]')
    
    date2_input.click()

    time.sleep(2)

    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    time.sleep(20)


    driver.quit()
