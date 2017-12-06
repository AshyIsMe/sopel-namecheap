from __future__ import print_function

from bs4 import BeautifulSoup
from selenium import webdriver

BASE_URL = 'https://www.namecheap.com/domains/registration/results.aspx?domain='

def find_domains(domainsearch):
    driver = webdriver.PhantomJS()
    driver.get(BASE_URL + domainsearch)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    domains = []
    for li in soup.find_all('li', {"class": "register"}):
        domain = li.find('span', {"class": "domain-name"})
        price = li.find('span', {"class": "domain-dollar-value"})
        if domain and price:
           domains.append(domain.text + ' ' +  price.text.replace('year', 'yr'))
    return domains

if __name__ == "__main__":
    domains = find_domains('plzbum.lol')
    print(", ".join(domains))
