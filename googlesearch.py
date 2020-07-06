from googlesearch import search
query='Bringham Young University Study Point'
query = query.split()
query = '+'.join(query)

for j in search(query, tld='com', num=2, stop=1, pause=2):
    print(j)