
from googlesearch import search

def search_google(query, num_results=1):
    search_results = []
    try:
        # Perform Google search and get URLs of search results
        for url in search(query, num_results=num_results):
            search_results.append(url)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return search_results
