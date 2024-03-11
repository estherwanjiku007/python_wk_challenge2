from article import Article
from magazine import Magazine
class Author:
    all=[]
    def __init__(self,name):
        self._name=name 
        Author.all.append(self)
       # Author.checksattr(self.name,self)
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str) and 5<=len(name)<=50 :
            self._name=name
        else:print(ValueError("Name must be a valid string of length between 5 and 50 characters"))

    def articles(self):
        my_articles=[articles for articles in Article.all if Article.author==self ]
        return my_articles
    
    def  magazines(self):
        my_magazines=[magazines for magazines in Magazine.all if Magazine.name==self]
        return my_magazines
    
    def add_article(self,magazine,title):
        Article.title=title
        Article.magazine=magazine


       # Author.checksattr(name,self)      
    
    # @property
    # def name(self):
    #     return self._name
    
    # @classmethod
    # def checksattr(cls,name,self):
    #    # print(cls.__name__)
    #     if hasattr(Author,self.name) and isinstance(name,str) and 1<=len(name):
    #         #print(cls.__name__)
    #         self.name=name
    #         print(name)
      #  else:raise ValueError("Name must be valid and should be a string of length greater than one")


       
    # @classmethod
    # def checks_attr(cls,name):
    #     if hasattr(Author.__name__,name)==True:
    #         print(cls.__name__)
    #         return cls.__name__
        #else:print(ValueError("The author_name should be valid"))

        

