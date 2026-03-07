class Book:

    def __init__(self,title,author,list_of_reviews):
        self.title = title
        self.author = author
        self.list_of_reviews = [list_of_reviews]
        

    def new_review(self,review):
        self.list_of_reviews.append(review)
        print("Review Successfully Added")
        

    def count_reviews(self):
        print(f"Total Number Of reviews = {len(self.list_of_reviews)}")

    def display_reviews(self):
        for review in self.list_of_reviews:
            print(review)

book1 = Book("car","Abhishek","Good Book")
print(book1.list_of_reviews)
book1.new_review("Very Nice Book")
print(book1.list_of_reviews)
book1.count_reviews()
book1.display_reviews()

