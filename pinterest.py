import requests

access_token = 'pina_AMAS5RAWABNIKAAAGDAN4CP5HGDV7CYBQBIQCXTJDYKOW5452WNGLPGWQADI32VI5XUSXYXHSD5XZDNT56BLH7SNFNYZNGQA'
access_token2 = 'pina_AMAS5RAWABNIKAAAGDAN4CPGSSDV7CYBACGSOIHBNFEKWIE2YSA7FXMULHFJQ2CRQ5UN6XIYP2O3YBDKHUWX4LTDB7WJ4GIA'
board_id = '<Your Board ID>'
note = '<Note for the pin>'
link = '<Link for the pin>'
image_url = '<Image URL for the pin>'

url = 'https://api.pinterest.com/v1/pins/'
params = {      
    'access_token': access_token,
    'board': board_id,
    'note': note,
    'link': link,
    'image_url': image_url
}

response = requests.post(url, params=params)

if response.status_code == 201:
    print("Pin created successfully")
else:
    print("Failed to create pin. Response code:", response.status_code)