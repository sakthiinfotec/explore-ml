import pandas as pd
from pytrends.request import TrendReq

ML = "Machine Learning"
trends = TrendReq()
# trends.build_payload(kw_list=[ML])
# data = trends.interest_by_region()
# data = data.sort_values(by=ML, ascending=False)
# data = data.head(10)
# print(data)

india_trends = trends.realtime_trending_searches(pn='US')
top_10_india_trends = india_trends.head(10)
print(top_10_india_trends)
