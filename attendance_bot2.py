UID = 'YOUR-UID'
password = 'YOUR-PASSWORD'
##################################################################

from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common import by
from selenium import webdriver
import time
import datetime

##############################################
BEEE_code = "course-link-_16227_1"

BEEE_lab_code = "course-link-_16194_1"

maths_code = "course-link-_17319_1"

english_code = "course-link-_16938_1"

english_lab_code = "course-link-_16831_1"

iot_code = "course-link-_15948_1"

cpp_code = "course-link-_15785_1"

cpp_lab_code = "course-link-_15488_1"

physics_code = "course-link-_17539_1"

physics_lab_code = "course-list-course-_17473_1"

mentoring_code = "course-link-_17964_1"

comp_work_code = "course-link-_15638_1"

maths_all_code = "course-link-_17317_1"

##########################################################################
print("COPYRIGHT KARAN SHARMA (20BET1080)")

driver = webdriver.Firefox()
driver.get("https://cuchd.blackboard.com/?new_loc=%2Fultra%2Fcourse")
time.sleep(5)
elem = driver.find_element_by_tag_name("body")
opt = Options()
dayofweek = datetime.datetime.today().strftime("%A")


def login():
    try:
        ok_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "agree_button"))
        )
        ok_button.click()
    except:
        pass    

    time.sleep(2)

    usr_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user_id"))
    )
    usr_name.send_keys(UID)
    time.sleep(2)

    passwod = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    passwod.send_keys(password)
    time.sleep(2)

    login_but = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "entry-login"))
    )
    login_but.click()
    time.sleep(10)


def BEEE():
    button_ = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, BEEE_code))
    )
    button_.click()
    time.sleep(1)

def BEEE_lab():
    button_ = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, BEEE_lab_code))
    )
    button_.click()
    time.sleep(1)

def maths():
    button_ = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, maths_code))
    )
    button_.click()
    time.sleep(1)

def english():
    button_ = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, english_code))
    )
    button_.click()
    time.sleep(1)
def english_lab():
    button_ = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, english_lab_code))
    )
    button_.click()
    time.sleep(1)
def iot():
    button_ = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, iot_code))
    )
    button_.click()
    time.sleep(1)

def cpp():
    button_ = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, cpp_code))
    )
    button_.click()
    time.sleep(1)
def cpp_lab():
    button_ = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, cpp_lab_code))
    )
    button_.click()
    time.sleep(1)

def physics():
    button_ = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, physics_code))
    )
    button_.click()
    time.sleep(1)
def physics_lab():
    button_ = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, physics_lab_code))
    )
    button_.click()
    time.sleep(1)

def mentoring():
    button_ = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, mentoring_code))
    )
    button_.click()
    time.sleep(1)

def computer_workshop():
    button_ = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, comp_work_code))
    )
    button_.click()
    time.sleep(1)

def maths_all():
    button_ = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, maths_all_code))
    )
    button_.click()
    time.sleep(1)

def class_():
    button_ = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"dropdown"))
    )
    button_.click()
    time.sleep(1)

if dayofweek == "Monday":
    login()
    BEEE_lab()
    class_()
elif dayofweek == "Tuesday":
    login()
    computer_workshop()
    class_
elif dayofweek == "Wednesday":
    login()
    maths_all()
    class_()
elif dayofweek == "Thursday":
    login()
    physics_lab()
    class_()
elif dayofweek == "Friday":
    login()
    cpp()
    class_()