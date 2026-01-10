from textblob import TextBlob
line=TextBlob("I would hate to learn AI")
print(f"polarity:{line.sentiment.polarity}")
p= line.sentiment.polarity
if p == -1.0:
    print("100% negative sentence ")