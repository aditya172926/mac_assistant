from googlesearch import search

def search_for_website(query):
    query = query.split()
    query = '+'.join(query)

    for j in search(query, tld='com', num=2, stop=1, pause=2):
        print(j)
    return j