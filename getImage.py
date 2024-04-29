from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time





def gettingImage(serchWord,num):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=  chrome_options )

    # driver = webdriver.Chrome()

    # user_input = input("Enter your search query: ")
    user_input = serchWord


    driver.get("https://images.google.com/")


    focused_element = driver.switch_to.active_element


    focused_element.send_keys(user_input)
    focused_element.send_keys(Keys.ENTER)

    # Retrieve the image sources
    time.sleep(5)
    image_element = driver.find_element(By.CSS_SELECTOR,'#center_col img')
    image_element.click()
    time.sleep(1)
    #SIDE BAR == id="Sva75c"

    sidebar = driver.find_element(By.ID,"Sva75c")
    sideImg = sidebar.find_element(By.CSS_SELECTOR,".jlTjKd img")

    arr = []
    for i in range(num):
        time.sleep(2)
        sidebar = driver.find_element(By.ID,"Sva75c")#HJRshd
        focused_element = driver.switch_to.active_element
        focused_element.send_keys(Keys.ARROW_RIGHT)

        time.sleep(2)
        sideImg = sidebar.find_element(By.CSS_SELECTOR,".jlTjKd img")
        source = sideImg.get_attribute("src")

        arr.append(source)
    
    driver.quit()
    return arr

    









# print(image_sources)

# with open("test011s.txt","w") as file:
#     file.write(str(image_sources))