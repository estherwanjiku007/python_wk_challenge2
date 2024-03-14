class Article:
    def __init__(self,title,author,magazine) -> None:
       if not isinstance(title,str) or len(title) <5 or len(title)>50:
           raise ValueError("Title must be str and btwn 5 and 50 characters ")
       if not isinstance(author,Author) :
           raise ValueError("Author must be an insatance of Author")
       if not isinstance(magazine,Magazine) :
           raise ValueError("Author must be an insatance of Author")
       
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
       
       
       



    