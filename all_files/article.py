from author import Author
from magazine import Magazine
class Article:
    all=[]
    def __init__(self,author,magazine,title):
        self._author=author
        self._magazine=magazine
        self._title=title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if hasattr(Article,self._title) and isinstance(title,str) and 5<=len(title)>=50:
            self._title=title
        else:raise ValueError("Title should be string of length between 5 and 50 characters")
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,author):
     if isinstance(author,Author):
         self._author=author
     else:print(ValueError("Author must be an instance of authors"))

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self,magazine):
        if isinstance(magazine,Magazine):
            self._magazine=magazine
        else:print(ValueError("Magazine must be an instance of magazines"))



        


    