
from bs4 import BeautifulSoup
from selenium import webdriver

def find_domains(domainsearch):
    driver = webdriver.PhantomJS()
    driver.get('https://www.namecheap.com/domains/registration/results.aspx?domain='
            + domainsearch)

    html = driver.page_source
    soup = BeautifulSoup(html)

    for tag in soup.find_all('li', {"class": "register"}):
        print tag.text

if __name__ == "__main__":
    find_domains('plzbum.lol')
