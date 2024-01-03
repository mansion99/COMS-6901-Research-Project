import csv
from eventregistry import *
er = EventRegistry(apiKey = '04c61023-5016-4927-9e49-ba2682c8ac48')

# India_query = {
#     "$query": {
#         "$and": [
#             {
#                 "$or": [
#                     {
#                         "conceptUri": "http://en.wikipedia.org/wiki/Climate_change"
#                     },
#                     {
#                         "conceptUri": "http://en.wikipedia.org/wiki/Climate_variability_and_change"
#                     },
#                     {
#                         "conceptUri": "http://en.wikipedia.org/wiki/Climate_change_mitigation"
#                     },
#                     {
#                         "conceptUri": "http://en.wikipedia.org/wiki/Paris_Agreement"
#                     },
#                     {
#                         "conceptUri": "http://en.wikipedia.org/wiki/Climate_crisis"
#                     },
#                     {
#                         "conceptUri": "http://en.wikipedia.org/wiki/Climate_change_denial"
#                     },
#                     {
#                         "conceptUri": "http://en.wikipedia.org/wiki/Effects_of_climate_change"
#                     },
#                     {
#                         "conceptUri": "http://en.wikipedia.org/wiki/Climate_change_adaptation"
#                     }
#                 ]
#             },
#             {
#                 "locationUri": "http://en.wikipedia.org/wiki/India"
#             },
#             {
#                 "$or": [
#                     {
#                         "sourceUri": "timesofindia.indiatimes.com"
#                     },
#                     {
#                         "sourceUri": "thehindu.com"
#                     },
#                     {
#                         "sourceUri": "hindustantimes.com"
#                     }
#                 ]
#             },
#             {
#                 "dateStart": "2013-01-01",
#                 "lang": "eng"
#             }
#         ]
#     },
#     "$filter": {
#         "isDuplicate": "skipDuplicates"
#     }
# }

US_query = {
    "$query": {
        "$and": [
            {
                "$or": [
                    {
                        "conceptUri": "http://en.wikipedia.org/wiki/Climate_change"
                    },
                    {
                        "conceptUri": "http://en.wikipedia.org/wiki/Climate_variability_and_change"
                    },
                    {
                        "conceptUri": "http://en.wikipedia.org/wiki/Climate_change_mitigation"
                    },
                    {
                        "conceptUri": "http://en.wikipedia.org/wiki/Paris_Agreement"
                    },
                    {
                        "conceptUri": "http://en.wikipedia.org/wiki/Effects_of_climate_change"
                    },
                    {
                        "conceptUri": "http://en.wikipedia.org/wiki/Climate_change_denial"
                    },
                    {
                        "conceptUri": "http://en.wikipedia.org/wiki/Climate_change_adaptation"
                    }
                ]
            },
            {
                "locationUri": "http://en.wikipedia.org/wiki/United_States"
            },
            {
                "$or": [
                    {
                        "sourceUri": "washingtonpost.com"
                    },
                    {
                        "sourceUri": "nytimes.com"
                    },
                    {
                        "sourceUri": "nypost.com"
                    },
                    {
                        "sourceUri": "foxnews.com"
                    },
                    {
                        "sourceUri": "us.cnn.com"
                    }
                ]
            },
            {
                "dateStart": "2016-01-01",
                "dateEnd": "2023-11-20",
                "lang": "eng"
            }
        ]
    }
}

q = QueryArticlesIter.initWithComplexQuery(US_query)

# Define the CSV file name
csv_file = "USA_news_data.csv"

# Open the CSV file for writing
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Source', 'Title', 'Author', 'Content/Description', 'Date'])

    # Execute the query and iterate over articles
    # articles = q.execQuery(er, maxItems=10)  # Reduced maxItems for testing
    # print(articles)
    # print("Number of articles fetched:", len(articles))  # Check the number of articles

    for article in q.execQuery(er, maxItems=10000):
            source = article.get('source', {}).get('title', '')
            title = article.get('title', '')
            
            # Extracting author names
            author_names = [author.get('name', '') for author in article.get('authors', [])]
            author = ', '.join(author_names)

            content = article.get('body', '') or article.get('summary', '')
            date = article.get('dateTime', '')
            writer.writerow([source, title, author, content, date])

print("Data retrieval complete. Check the CSV file:", csv_file)