
def pesquisar():
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 

    query = "Youtube"
        
    for j in search(query, tld="co.in", num=30, stop=30, pause=2): 
        print(j) 
pesquisar()
