from article import Article
from author import Author
from magazine import Magazine

try: 
  #create an author instance 
  all_author1 = Author("Esther")
  print("Author name" , all_author1.name)

  # test other methods 

except ValueError as e:
    print("error author isntance " , e)

# testing 
# magazine
try: 
  #create an author instance 
  magazine1 = Magazine("money", "Finances")
  magazine2 = Magazine("Technology", "Progrmme design")
  print("Magazine name: " , magazine1.name)
  print("Magazine category: " , magazine1.category)
  # test other methods 

except ValueError as e:
    print("error author isntance " , e)

# testing 
# article
try: 
  #create an author instance 
  author2 = Author("Wanjiku")
  article1 = Article("The future of AI",all_author1, magazine1, )
  article2 = Article("The Daily Tech",all_author1, magazine1)
  article3 = Article("Germination Process",author2,magazine2)
  print("Article name: " , article1.title)
  print("Article author: " , article1.author.name)
  print("Article magazine: " , article1.magazine.name)
  # test other methods 

except ValueError as e:
    print("error author instance " , e)

# Testing additional methods and relationships
try: 
  article4 = all_author1.add_articles(magazine1, "AI Trends")
  article5 = all_author1.add_articles(magazine2, "Science Breakthroughs")
  article6 = author2.add_articles(magazine1, "ML applications")

  print("\n Author's articles ")
  for article in all_author1.articles():
    print("-" , article.title)

    # magazine authors 
    #  contributig authors 
except ValueError as e:
    print("error author isntance " , e)


# Testing top_publisher method
try: 
    top_magazine = Magazine.top_publisher()
    if top_magazine:
       print("\n Top Publisher: " , top_magazine.name)
    else: 
       print("\n Articles not sufficient,top publisher cannot be determined.")
except ValueError as e:
    print("error author isntance " , e)