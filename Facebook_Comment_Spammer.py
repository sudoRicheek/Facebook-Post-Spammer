from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import time

###Global variables
driver = None

###Loads the chromedriver and disables the notifications in chrome
def load_driver():
	global driver
	chromedriver = os.path.abspath("./chromedriver.exe")
	os.environ["webdriver.chrome.driver"] = chromedriver	
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chromedriver, chrome_options=options)			#opens the browser
    ###The above specifies the path to the chromedriver.exe(for Windows)

###Welcome screen in console
def welcome_screen():
    print("Facebook Comment Spammer : Build INFO : 1.00")
    print("Selenium : 3.141.0")
    print("ChromeDriver 80.0.3987.106 \n")
    print("!!! It is recommended that you don't use your primary FB account to do the spam !!!")
    print()

###For disabling any active notifications that might pop-up after opening Facebook


###Take the Spam info :
def get_post_info():
    global driver
    person_to_be_spammed = input("Enter Username of person to be spammed : ")   #Username
    post_to_be_spammed = input("Enter Post ID of the person to be spammed : ")  #POST ID is the number that appears at the end of each post URL
    driver.get("https://www.facebook.com/" + person_to_be_spammed + "/posts/" + post_to_be_spammed)
    print("Wait...")
    time.sleep(2)
    return person_to_be_spammed, post_to_be_spammed

###Take Info and LOGIN into Facebook and move to mobile version of FB as it doesn't use Javascript
def log_in(person_to_be_spammed, post_to_be_spammed):
    global driver
    
    ###Take EMAIL
    emailelem = driver.find_element_by_xpath('//*[@id="email"]')
    your_email = input("Enter your Email registered with FB : ")
    emailelem.clear()
    emailelem.send_keys(your_email)
    
    ###Take PASSWORD
    passelem = driver.find_element_by_xpath('//*[@id="pass"]')
    your_pass = input("Enter your FB password : ")
    passelem.clear()
    passelem.send_keys(your_pass)
    time.sleep(1)
    
    print("Wait...")
    
    ###PRESS LOGINBUTTON
    loginbuttonelem = driver.find_element_by_xpath('//*[@id="loginbutton"]')
    loginbuttonelem.click()
    time.sleep(10) ###change to wait for getting the loaded www.facebook
    
    driver.get('https://m.facebook.com/' + person_to_be_spammed + '/posts/' + post_to_be_spammed)
    #Wait for the mobile version to load
    time.sleep(7) ###change to wait for the m.facebook to load

#We need to randomize the delay and the text to be commented, if we are spamming on FB, otherwise
#your account can get banned/ caught for suspicious activities

###Gets the spam info. THIS FUCNTION NEEDS MORE FEATURES
def get_spam_info():
    message = input("Enter the text to be commented : ")
    no_of_spams = input("Enter the number of time you want the comment to replicate : ")
    
    print("\n Now just wait for the comments to be posted ! ")
    return message, no_of_spams


###Types comments and posts
def spammer_method(message, no_of_spams):
    for number_of_posted in range(int(no_of_spams)):
    	commentelement = driver.find_element_by_xpath("//*[@id='composerInput']")
    	commentelement.click()
    	commentelement.clear()
    	commentelement.send_keys(message)
    	time.sleep(1) #Delay time for the post button to get active
    	postbutton = driver.find_element_by_xpath('//*[@name="submit"]')
    	postbutton.click()
    	time.sleep(4) #Delay time for the post button to reset

def final_work():
    time.sleep(30) ###JUST for displaying the final stuff
    driver.close()
    
    
###Define the main function
def main():
    load_driver()
    welcome_screen()
    post_info = get_post_info()
    log_in(post_info[0], post_info[1])
    spam_info = get_spam_info()
    spammer_method(spam_info[0], spam_info[1])
    final_work()
    
if __name__ == "__main__":
    main()
####INSERT AN EXCEPTION HANDLER TO CLOSE THE DRIVER, IN CASE OF ANY EXCEPTION
