import facebook

""">pip install facebook-sdk"""

graph = facebook.GraphAPI(access_token="", version="2.12")

def procurarLugares(local):
    # Procura por lugares na região da avenida paulista, colocamos a longitude e latitude.
    print(local)
    places = graph.search(type='place',
                      center=local,
                      fields='name,location')
    
    # para cada local ele retorna um objeto, na qual podemos exebir na tela suas informações
    for place in places['data']:
        print('%s %s' % (place['name'].encode(),place['location'].get('zip')))

"""
Av Paulista= -23.5629, -46.6544

Faculdade = -23.525765, -46.649121

"""

def putRegiao():
    latitude = input("Digite a latitude desejada: ")
    longitude = input("Digite a longitude Desejada :")
    local=latitude +","+ longitude
    procurarLugares(local)

putRegiao()
    