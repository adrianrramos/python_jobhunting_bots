from my_credentials import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

EMAIL = ANGEL_LIST_EMAIL
PASSWORD = ANGEL_LIST_PASSWORD

PATH = CHROME_DRVIER_PATH


driver = webdriver.Chrome(PATH)

driver.get("https://angel.co/jobs")

# LOGGING IN
login_link = driver.find_element_by_class_name("link_2e8cf")
login_link.click()
time.sleep(3)

email_input = driver.find_element_by_id("user_email")
email_input.send_keys(EMAIL)

password_input = driver.find_element_by_id("user_password")
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)
time.sleep(3)

print("loading project...")

# AUTOMATE APPLY


def work_current_page():
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(10)

    jobs_card_list = driver.find_elements_by_class_name("component_4d072")

    for job_card in jobs_card_list:

        apply_button = job_card.find_element_by_class_name(
            "styles_component__3A0_k")
        apply_button.click()
        time.sleep(3)

        job_card_modal = driver.find_element_by_class_name(
            "ReactModal__Content--after-open")

        card_header = job_card_modal.find_element_by_class_name(
            "startup_5f07e")
        company_name = card_header.find_element_by_class_name(
            "component_21e4d")

        text_area = job_card_modal.find_element_by_id("form-input--userNote")
        text_area.send_keys("Hello there, I am a front end developer who loves working with cutting edge tools and building web applications. I see that  {} is looking for help in this department. What I offer to bring to the {} developer team is a hand in engineering solutions for any and all front end problems. Working with your team would  help me grow as a developer, and give me the experience that would otherwise be impossible to get outside of your organization. I hope what I’m saying resonates with your company's goals. If you would like to learn more about me, please contact me as soon as possible Sincerely, Adrian Ramos".format(company_name.text, company_name.text))

        submit_app_button = job_card_modal.find_elements_by_class_name(
            "styles_component__3A0_k")[1]
        submit_app_button.click()

        time.sleep(2)


i = 0

while True:
    i = i + 1

    print("working on iteration #{}...".format(i))
    work_current_page()
    driver.refresh()
    print("finished iteration #{}".format(i))
