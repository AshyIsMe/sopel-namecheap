
from bs4 import BeautifulSoup
from selenium import webdriver

def find_domains(domainsearch):
    driver = webdriver.PhantomJS()
    driver.get('https://www.namecheap.com/domains/registration/results.aspx?domain='
            + domainsearch)

    html = driver.page_source
    soup = BeautifulSoup(html)

    domains = ""
    for li in soup.find_all('li', {"class": "register"}):
        domain = li.find('span', {"class": "domain-name"})
        price = li.find('span', {"class": "domain-dollar-value"})
        #print domain.text + ' ' +  price.text.replace('year', 'yr') + ', '
        domains += domain.text + ' ' +  price.text.replace('year', 'yr') + ', '

    return domains

if __name__ == "__main__":
    domains = find_domains('plzbum.lol')
    print domains
