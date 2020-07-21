from EmailLibTest import *
import re


def getMPPG1info(email):
    reSearches = ['(Here are the MPPG credentials for) (.*)',
                  '(Street Address 1:) (.*)',
                  '(City:) (.*)',
                  '(State:) (.*)',
                  '(Zip:) (.*)',
                  '(Contact First Name:) (.*)',
                  '(Contact Last Name:) (.*)',
                  '(Phone:) (.*)',
                  '(email:) (.*)',
                  '(Store ID:) (.*)',
                  '(Merchant ID:) (.*)',
                  '(Terminal ID:) (.*)',
                  '(Store ID:) (.*)',
                  '(Processor Name:) (.*)',
                  '(MPPG Merchant ID =) (.*)']
    reSearches = ['Here are the MPPG credentials for',
                  'Street Address 1:',
                  'City:',
                  'State:',
                  'Zip:',
                  'Contact First Name:',
                  'Contact Last Name:',
                  'Phone:',
                  'email:',
                  'Store ID:',
                  'Merchant ID:',
                  'Terminal ID:',
                  'Store ID:',
                  'Processor Name:',
                  'MPPG Merchant ID =']
    reSearches = ['Here are the MPPG credentials for']

    for i in range(len(reSearches)):
        match = re.search(r"(reSearches[i]) (.*)", email)
        emailinfo = match.group(2)
        return emailinfo





def getNameOfSite(email):
    match = re.search(r"(Here are the MPPG credentials for) (.*)", email)
    # print(match.group(2))
    nameOfSite = match.group(2)
    return nameOfSite

def getAddress(email):
    match = re.search(r"(Street Address 1:) (.*)", email)
    siteAddress = match.group(2)
    match = (re.search(r"(Street Address 2:) (.*)", email))
    siteAddress += match.group(2)
    return siteAddress

def getCity(email):
    match = re.search(r"(City:) (.*)", email)
    siteCity = match.group(2)
    return siteCity

def getState(email):
    match = re.search(r"(State:) (.*)", email)
    siteState = match.group(2)
    return siteState

def getOutGoingEmail(updatedEmail):
    match = re.search(r"(Email:) (.*)", updatedEmail)
    # print(match.group(2))
    outGoingEmail = match.group(2)
    return outGoingEmail

def getMPMnumber(updatedEmail):
    match = re.search(r"(MPPG Merchant ID =) (.*)", updatedEmail)
    # print(match.group(2))
    mpmNumber = match.group(2)
    return mpmNumber

def getTerminalID(updatedEmail):
    match = re.search(r"(Terminal ID:) (.*)", updatedEmail)
    # print(match.group(2))
    terminalID = match.group(2)
    return terminalID







if __name__ == "__main__":
    for filename in os.listdir('../EmailNotYetProcessed'):
        os.chdir('../EmailNotYetProcessed')
        emailBody = printEmailBody(filename)
        #getMPPG1info(emailBody)
        try:
            print(getNameOfSite(emailBody))
            print(getAddress(emailBody))
            print(getCity(emailBody))
            print(getState(emailBody))
            print(getOutGoingEmail(emailBody))
        except AttributeError as e:
            print(filename)
            print(emailBody)






        print("\n\n\n")