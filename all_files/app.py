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
        return article_titles.name

    def contributing_authors(self):
        matching_authors=[]
        matching_authors2=[]
        if Article.magazine==self:
            matching_authors.append(Article.author)
        for a in range(len(matching_authors)):
            if matching_authors.count(matching_authors[a]>2):
                matching_authors2.append(matching_authors[a])
        return matching_authors2       
        
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
        try:
            if isinstance(name,str) and 1<=len(name) :
              self._name=name
        except:print(ValueError("Name must be a valid string of length greater than zero"))

    def articles(self):
        my_articles=[articles for articles in Article.all if Article.author==self ]
        return my_articles
    
    def  magazines(self):
        my_magazines=[magazines for magazines in Magazine.all if Magazine.name==self]
        return my_magazines
    
    def add_article(self,magazine,title):
        Article.title=title
        Article.magazine=magazine
        Article.author=Author(self.name) 
        Article.all.append(self)

    
    def topic_areas(self):
        contributed_articles=[]
        if Magazine.name==self:
            contributed_articles.append(Magazine.category)
        else :return None

Esther=Author(7)
print(Esther.name)

 

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

        


            

        

#standard=Magazine("Standard","")  
# print(standard._name)    
# print(standard._category)