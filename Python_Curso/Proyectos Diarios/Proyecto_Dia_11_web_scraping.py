import bs4
import requests


url_base = 'http://books.toscrape.com/catalogue/page-{}.html'


titulos_rating_alto = []

for p in range(1, 51):
    url_pagina = url_base.format(p)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text,'html.parser')

    libros = sopa.select('.product_pod')

    for l in libros:

        if len(l.select('.star-rating.Four')) != 0 or len(l.select('.star-rating.Five')):
            titulo_libro = l.select('a')[1]['title']
            titulos_rating_alto.append(titulo_libro)


for t in titulos_rating_alto:
    print(t)



