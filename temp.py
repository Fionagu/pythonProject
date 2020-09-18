def getMaxNum(reviewscore):
    scores = [int(x) for x in reviewscore]
    print(max(scores))

reviewscore = ['2','3','4']
print(getMaxNum(reviewscore))
