import xplore
import json

from config import api_key

def pretty_print(a):
    """Print a readable citation of an article"""
    print(f"Vol. {a['volume']} Issue {a['issue']} ({a['publication_date']}), pp. {a['start_page']}-{a['end_page']} - DOI {a['doi']} ({a['access_type']})")
    print(a['title'])
    for auth in a['authors']['authors']:
        print(f"{auth['full_name']} ({auth['affiliation']}) ", end='')
    print()
    print()


if __name__=='__main__':
    query = xplore.xploreapi.XPLORE(api_key)
    query.issn('1520-9202')
    query.publicationYear('2018')
    query.maximumResults(200)
    response = query.callAPI()
    data = json.loads(response)
    # print(data)

    articles = data['articles']
    articles = [a for a in articles if a['access_type']!='EPHEMERA']
    articles.sort(key=lambda a: int(a['start_page']))
    articles.sort(key=lambda a: int(a['issue']))
    for article in articles:
        # print(article)
        pretty_print(article)

# url='http://ieeexploreapi.ieee.org/api/v1/search/articles?apikey=7dy2zxycpp87wrgdnhcx6e5k&format=json&max_records=100&start_record=1&sort_order=asc&sort_field=publication_year&issn=1520-9202&publication_year=2018'

