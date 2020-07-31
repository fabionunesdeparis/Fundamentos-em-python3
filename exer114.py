# @Fábio C Nunes - 07.07
import requests
try:
    r = requests.get('http://www.pudim.com.br')
except:
    print('\033[41m O site não está acessivél \033[m')
else:
    print('\033[42m O site está acessivél \033[m')
