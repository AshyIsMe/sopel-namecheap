# sopel-namecheap

Namecheap domain lookup script for Sopel IRC bot.

## Installation

Tested on Ubuntu 1604LTS. Requires BeautifulSoup, selenium and phantomjs.

```
sudo pip3 install BeautifulSoup selenium
```

The default Ubuntu phantomjs package appears to have issues. Download the
static build here http://phantomjs.org/download.html.  Requirements:

```
sudo apt-get install libfreetype6 libfontconfig1 -y
```

Make sure the phantomjs binary is in your $PATH.

## Testing

```
python3 namecheap.py plzbum.lol
plzbum.lol 33.99/yr, plzbum.nyc 16.92/yr, plzbum.co 11.66/yr, plzbum.life 2.47/yr, plzbum.services 2.47/yr, plzbum.online 1.16/yr, plzbum.fun 1.16/yr, plzbum.club 1.01/yr, plzbum.pw 1.16/yr, plzbum.live 5.10/yr, plzbum.store 6.41/yr, plzbum.net 16.92/yr, plzbum.org 13.12/yr, plzbum.accountant 0.63/yr, plzbum.io 43.19/yr, plzbum.tech 1.16/yr, plzbum.info 2.61/yr, plzbum.loan 0.63/yr, plzbum.download 0.63/yr, plzbum.host 1.16/yr, plzbum.bid 0.63/yr, plzbum.review 0.63/yr, plzbum.party 0.63/yr, plzbum.date 0.63/yr, plzbum.science 0.63/yr, plzbum.website 1.16/yr
```

