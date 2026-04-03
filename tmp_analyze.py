import pandas as pd
import json

file_path = "d:/Antigravity/lovemoneygame.cc/26年3月lovemoneygame.cc 每月GSC数据_无标题页面_表格.csv"
df = pd.read_csv(file_path)

# Normalize queries: lower case, strip whitespace
df['Query_Norm'] = df['Query'].str.lower().str.strip()

# Overall agg by Query
query_agg = df.groupby('Query_Norm').agg({
    'Impressions': 'sum',
    'Url Clicks': 'sum',
    'URL CTR': 'mean',
    'Average Position': 'mean'
}).reset_index().sort_values('Impressions', ascending=False)

# Get top 300 queries
top_queries = query_agg.head(300).to_dict(orient='records')

# Get mapping of query to top landing page
top_lps = df.groupby(['Query_Norm', 'Landing Page']).agg({'Impressions': 'sum'}).reset_index()
idx = top_lps.groupby('Query_Norm')['Impressions'].idxmax()
top_lps = top_lps.loc[idx]

lp_dict = dict(zip(top_lps['Query_Norm'], top_lps['Landing Page']))
for q in top_queries:
    q['Landing Page'] = lp_dict.get(q['Query_Norm'])

with open('qu.json', 'w', encoding='utf-8') as f:
    json.dump(top_queries, f, ensure_ascii=False, indent=2)

lp_agg = df.groupby('Landing Page').agg({
    'Impressions': 'sum',
    'Url Clicks': 'sum'
}).reset_index().sort_values('Impressions', ascending=False)
lp_agg.to_csv('lps.csv', index=False)
