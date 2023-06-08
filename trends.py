from pytrends.request import TrendReq

pytrend = TrendReq()
pytrend.build_payload(
    kw_list=['Web Design 2023'])
related_queries_dict = pytrend.related_queries()

print(related_queries_dict)

# Get Google Keyword Suggestions
suggestions_dict = pytrend.suggestions(keyword='Web Design')
print(suggestions_dict[1]['title'])
