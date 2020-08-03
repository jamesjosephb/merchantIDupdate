from email import policy
from email.parser import BytesParser
import os
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import config


# Accepts email and returns body of email
def printEmailBody(emailFile):
    with open(emailFile, 'rb') as fp:
        msg = BytesParser(policy=policy.default).parse(fp)
    text = msg.get_body(preferencelist='plain').get_content()
    #print(msg['from'])
    #print(text)
    #print('\n\n\n')
    return text


# Accepts directery to save file and email to save then saves to directory
def EmailtoText(dir, emailFile):
    with open(emailFile, 'rb') as fp:
        msg = BytesParser(policy=policy.default).parse(fp)
    text = msg.get_body(preferencelist='plain').get_content()
    emailFile = emailFile[:-4]
    emailFile = emailFile[3:]
    emailFile = emailFile.strip()
    os.chdir(dir)
    #emailtxt = open(emailFile + '.txt', 'w')
    #emailtxt.write(text)
    #emailtxt.close()
    for root, dirs, files in os.walk(os.getcwd()):
        if str(emailFile + '.txt') in files:
            #document.save(title + "(1)" + ".docx")
            emailtxt = open(emailFile + '(1)' + '.txt', 'w') # This should be fixed, If there are more then 2 then one is getting replaced
            emailtxt.write(text)
            emailtxt.close()
        else:
            emailtxt = open(emailFile + '.txt', 'w')
            emailtxt.write(text)
            emailtxt.close()


# Checks to ensure that data is in JSON format
def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True


# Accepts JSON and return MPM# and MID#
def retreaveMPMIDfromJSON(jsonData):
    json_object = json.loads(printEmailBody(filename))
    MPM = json_object["username"]
    MID = json_object["acceptorid"]
    return MPM, MID


# Logs into Support Database and returns Selenium driver object
def loginSupportDB():
    path = "../drivers/geckodriver"
    driver = webdriver.Firefox(executable_path=path)
    driver.get("https://www.mycryptopay.com/devel/genesys/index.php")
    driver.find_element_by_name("username").send_keys(config.username)
    driver.find_element_by_name("password").send_keys(config.password)
    driver.find_element_by_name("submit_login").click()
    return driver


# Accepts driver for Selenium oject that is logged into website(see loginSupportDB())
# Accepts MPM# and checks if MID# info is in Support Database if not it inserts MID#
def setDatabaseMPMID(driver, MPM, MID):
    driver.get("https://www.mycryptopay.com/devel/genesys/index.php?page=editcustomer&siteid=" + MPM)
    potentialExistingMID = driver.find_element_by_name("merchantid")
    print(potentialExistingMID.get_attribute("value"))
    if potentialExistingMID.get_attribute("value") == "":
        driver.find_element_by_name("merchantid").send_keys(MID)
        element = Select(driver.find_element_by_name('processor'))
        element.select_by_index(1)
        driver.find_element_by_name("submit_editcustomer").click()


if __name__ == "__main__":
    driver = loginSupportDB()
    for filename in os.listdir('../EmailNotYetProcessed'):
        os.chdir('../EmailNotYetProcessed')
        if filename.endswith(".eml"):
            if is_json(printEmailBody(filename)) == True:
                MPM, MID = retreaveMPMIDfromJSON(printEmailBody(filename))
                #print("MPM: %s" % MPM)
                #print("MPM: %s" % MID)
                EmailtoText('../JSONdata', filename)
                setDatabaseMPMID(driver, MPM, MID)
            else:
                EmailtoText('../nonJSONdata', filename)
        os.chdir('../EmailNotYetProcessed')
        os.remove(filename)
