from author import Author
from article import Article
class Magazine:
    all=[]
    def __init__(self,name,category):
        self.name=name
        self.category=category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name,str) and 2<=len(name)<=16:
            self._name=name
        else:raise ValueError("Name should be a string that has a length of between 2 and 16 characters")

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self,category):
        if isinstance(category,str) and  0<len(category):
            self._category=category
        else:raise ValueError("Category should be string that has a length greater than zero")
    def articles(self):
        all_articles=[aritcles for aritcles in Article.all if Article._magazine==self]
        return all_articles
    
    def contributors(self):
        all_authors=[authors for authors in Author.all if Author.name==Magazine.name  ]
        return all_authors
    
    def article_titles(self):
        article_titles=[all_titles for all_titles in Article.title if Article.magazine==self]
        return article_titles

    def contributing_authors(self):
        matching_authors=[]
        matching_authors2=[]
        if Article.magazine==self:
            matching_authors.append(Article.author)
        for a in range(len(matching_authors)):
            if matching_authors.count(matching_authors[a]>2):
                matching_authors2.append(matching_authors[a])
        return matching_authors2       
            
            

        

#standard=Magazine("Standard","")  
# print(standard._name)    
# print(standard._category)