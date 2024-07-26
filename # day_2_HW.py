# Question 1

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

def good_reviews():
    word = 'good'
    for review in python_reviews:
        if word in review:
            print(review)

good_reviews()

def excellent_review():
    word = 'excellent'
    for review in python_reviews:
        if word in review:
            print(review)

excellent_review()

def bad_review():
    word = 'bad'
    for review in python_reviews:
        if word in review:
            print(review)

bad_review()

def poor_review():
    word = 'poor'
    for review in python_reviews:
        if word in review:
            print(review)

poor_review()

def average_review():
    word = 'average'
    for review in python_reviews:
        if word in review:
            print(review)

average_review()

print('~'*50)

# Question 2

python_positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def positive_reviews():
    p_review_words = []
    total = len(p_review_words)
   

   
    word = 'good'
    for review in python_reviews:
        if word in review:
            p_review_words.append(word)
            print(review)
            count = 0
            count = count + 1
            print(f"This review has {count} positive word")
    word = 'excellent'
    for review in python_reviews:
        if word in review:
            p_review_words.append(word)
            print(review)
            count = 0
            count = count + 1
            print(f"This review has {count} positive word")
    word = 'great'
    for review in python_reviews:
        if word in review:
            p_review_words.append(word)
            print(review)
            count = 0
            count = count + 1
            print(f"This review has {count} positive word")
    word = 'awesome'
    for review in python_reviews:
        if word in review:
            p_review_words.append(word)
            print(review)
            count = 0
            count = count + 1
            print(f"This review has {count} positive word")
    word = 'fantastic'
    for review in python_reviews:
        if word in review:
            p_review_words.append(word)    
            print(review)
            count = 0
            count = count + 1
            print(f"This review has {count} positive word")
    word = 'superb'
    for review in python_reviews:
        if word in review:
            p_review_words.append(word)
            print(review)
            count = 0
            count = count + 1
            print(f"This review has {count} positive word")
    word = 'amazing'
    for review in python_reviews:
        if word in review:
            p_review_words.append(word)
            print(review)
            count = 0
            count = count + 1
            print(f"This review has {count} positive word")
           
   
    total = len(p_review_words)
    print(f"In your reviews, you have a total of: {total} positive reviews")

def negative_reviews():
    n_review_words = []
    total = len(n_review_words)
   

   
    word = 'poor'
    for review in python_reviews:
        if word in review:
            n_review_words.append(word)
            print(review)
            count = 0
            count = count + 1
            print(f"This review has {count} negative word")
    word = 'poor'
    for review in python_reviews:
        if word in review:
            n_review_words.append(word)
            print(review)
            count = 0
            count = count + 1
            print(f"This review has {count} negative word")
    word = 'terrible'
    for review in python_reviews:
        if word in review:
            n_review_words.append(word)
            print(review)
            count = 0
            count = count + 1
            print(f"This review has {count} negative word")
    word = 'horrible'
    for review in python_reviews:
        if word in review:
            n_review_words.append(word)
            print(review)
            count = 0
            count = count + 1
            print(f"This review has {count} negative word")
    word = 'awful'
    for review in python_reviews:
        if word in review:
            n_review_words.append(word)    
            print(review)
            count = 0
            count = count + 1
            print(f"This review has {count} negative word")
    word = 'disappointing'
    for review in python_reviews:
        if word in review:
            n_review_words.append(word)
            print(review)
            count = 0
            count = count + 1
            print(f"This review has {count} negative word")
    word = 'subpar'
    for review in python_reviews:
        if word in review:
            n_review_words.append(word)
            print(review)
            count = 0
            count = count + 1
            print(f"This review has {count} negative word")
           
   
    total = len(n_review_words)
    print(f"In your reviews, you have a total of: {total} negative reviews")




positive_reviews()

print('~'*50)

negative_reviews()


print('~'*50)
#-------------------------------------------------#

# Question 3

def summary_review():
    for review in python_reviews:
            print(review)
   
    print('-'*50)

    summary = review[0:31] + '...'
    print(summary)

summary_review()