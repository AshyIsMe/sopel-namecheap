#!/usr/bin/python

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

try:
    import sopel.module
except ImportError:
    # Probably running from commandline
    pass
else:
    @sopel.module.commands('namecheap')
    @sopel.module.example('.namecheap example.com')
    def f_namecheap(bot, trigger):
        """Look up a domain name with namecheap"""
        query = trigger.group(2).strip().lower()
        domains = find_domains(query)
        if len(domains):
            bot.say(", ".join(domains))
        else:
            bot.say("Couldn't query namecheap with: " + query)
        return sopel.module.NOLIMIT

if __name__ == "__main__":
    import sys
    query = 'example.com'
    if len(sys.argv) > 1:
       query = sys.argv[1]
    #print("Looking up {}".format(query))
    domains = find_domains(query)
    print(", ".join(domains))
