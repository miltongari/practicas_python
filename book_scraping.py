# Libreria para web scraping
# pip install requests
# pip install lxml
# pip install beautifulsoup4



import bs4
import requests

# crear url sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5 estrellas
titulos_ranting_alto = []

# iterar paginas

for pagina in range(1,51):

    # Crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')


    # Selecionar datos de los libros
    libros = sopa.select('.product_pod')

    # interar en los libros
    for libro in libros:

        #chequear que tenga 4 0 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0 :

            # guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']
            titulos_ranting_alto.append(titulo_libro)


# ver los libros de 4 y 5 estrellas en consolas
for t in titulos_ranting_alto:
    print(t)




