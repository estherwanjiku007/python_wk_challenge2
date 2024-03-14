
class Author:
    def __init__(self,name) :
           #Validating that the name is a str
           if not  isinstance(name,str) and   len(name)==0:           
             raise ValueError("Name should be a string which is not empty")
           self._name=name
           self._articles=[]

    @property
    def name(self):
        return self._name
    
    def articles(self):
        #Returning the list of articles te author has written
        return self._articles
    
    def add_articles(self,magazine,title):
        article=Article(title,self,magazine)
        self._articles.append(article)

    def magazines(self):
        #return all lists of  magazines that are unique
        return list(set(article.magazine for article in self._articles if isinstance(article.magazine,Magazine)))

    def topic_areas(self):
        if not self._articles:
            return None
       
        return list(set(article.category for article in self._articles if isinstance(article.author,Author)))
           
from article import Article
from magazine import Magazine
        


   