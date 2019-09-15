market={"dairy":["yogurt","cheese"],"fruits":['banana','apple','orange','lemon','apple','banana','banana']}
print(market)

market["candies"]=['mars','kinder','twix']
market["fruits"].sort()
set1=set(market["fruits"])
market["fruits"]=list(set1)
print(market)