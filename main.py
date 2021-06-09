#!/usr/bin/env python3

import re
from sre_constants import BRANCH
import emailer
from webscraping import WebScraping

padrao_email = "\w{2,50}@\w{2,15}\.[a-z]{2,3}"

while True:
    destinatario = input(str("Informe um email válido: "))
    _email = re.findall(padrao_email,destinatario)

    if not _email:
        print(f'Email Invalido! \n Ensira um email válido. ')
    else:
        break

    