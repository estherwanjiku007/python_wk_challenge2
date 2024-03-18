class Article:
    def __init__(self,title,author,magazine):
       if not isinstance(title,str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a str and btw 5 and 50 characters")
       if not isinstance(author,Author) :
           raise ValueError("author must be an instance of Author")
       if not isinstance(magazine,Magazine) :
           raise ValueError("Magazine must be an instance of Magazine")
       
       self._title=title
       self._author=author
       self._magazine=magazine

    @property
    def title(self):
        return self._title
       
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,value):
        if isinstance(value,Author):
            self._author=value
        else:raise ValueError("author must be of the Author instance")

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self,value):
        if isinstance(value,Magazine):
            self._magazine=value
        else:raise ValueError("Magazine should be an instance of Magazine class")

from author import Author
from magazine import Magazine
       
       
       



    