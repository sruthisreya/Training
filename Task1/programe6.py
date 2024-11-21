scores={"Alice":85,"Bob":90,"Charlie":75}
highest=max(scores,key=scores.get)
lowest=min(scores,key=scores.get)
print("highest:",highest)
print("lowest",lowest)