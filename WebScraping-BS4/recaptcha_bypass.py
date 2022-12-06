
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,requests
from A2T import audioToText

def pass_captcha(driver):
    delayTime = 2

    filename = '1.mp3'
    
    def saveFile(content,filename):
        with open(filename, "wb") as handle:
            for data in content.iter_content():
                handle.write(data)

    
    # driver.get(byPassUrl)
    # time.sleep(1)
    googleClass = driver.find_element(By.ID, 'captcha-v2')
    time.sleep(2)
    outeriframe = googleClass.find_element(By.TAG_NAME, 'iframe')
    time.sleep(1)
    outeriframe.click()
    time.sleep(2)
    allIframesLen = driver.find_elements(By.TAG_NAME, 'iframe')
    time.sleep(1)
    audioBtnFound = False
    audioBtnIndex = -1

    for index in range(len(allIframesLen)):
        driver.switch_to.default_content()
        iframe = driver.find_elements(By.TAG_NAME, 'iframe')[index]
        driver.switch_to.frame(iframe)
        driver.implicitly_wait(delayTime)
        try:
            audioBtn = driver.find_element(By.ID, 'recaptcha-audio-button') or driver.find_element(By.ID, 'recaptcha-anchor')
            audioBtn.click()
            audioBtnFound = True
            audioBtnIndex = index
            break
        except Exception as e:
            pass

    if audioBtnFound:
        try:
            while True:
                href = driver.find_element(By.ID,'audio-source').get_attribute('src')
                response = requests.get(href, stream=True)
                saveFile(response,filename)
                response = audioToText(filename)
                print(response)
                driver.switch_to.default_content()
                iframe = driver.find_elements(By.TAG_NAME, 'iframe')[audioBtnIndex]
                driver.switch_to.frame(iframe)
                inputbtn = driver.find_element(By.ID, 'audio-response')
                inputbtn.send_keys(response)
                inputbtn.send_keys(Keys.ENTER)
                time.sleep(2)
                errorMsg = driver.find_elements(By.CLASS_NAME, 'rc-audiochallenge-error-message')[0]
                if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                    print("Success")
                    driver.switch_to.default_content()
                    inputbtn = driver.find_element(By.ID, 'btn-submit')
                    inputbtn.send_keys(Keys.ENTER)
                    time.sleep(2)
                    inputbtn.send_keys(Keys.ENTER)
                    break
        except Exception as e:
                print(e)
                print('Caught. Need to change proxy now')
    else:
        print('Button not found. This should not happen.')
