class Article:
                  
    def __init__(self,title,author,magazine):
         
         if  isinstance(title,str) and 5<=len(title)>=50 :
            self.title=title
         else:raise Exception("Title should be string of length between 5 and 50 characters")
         if isinstance(author,Author):
           self.author=author
         else:raise Exception("Author must be an instance of authors")
         if isinstance(magazine,Magazine):
            self.magazine=magazine
         else:raise Exception("Magazine must be an instance of magazines")
        
         Article.all=[]
         Article.all.append(self)
    
    
class Magazine:
    
    def __init__(self,name,category):
        if isinstance(name,str) and 2<=len(name)<=16:
            self.name=name
        else:raise Exception("Name should be a string that has a length of between 2 and 16 characters")
        if isinstance(category,str) and  0<len(category):
            self.category=category
        else:raise Exception("Category should be string that has a length greater than zero")
        Magazine.authors=[]
        Magazine.all=[]
        Magazine.all.append(self)

    def articles_titles(self):
        all_articles=[aritcles for aritcles in Article.all if Article.magazine==self.name]
        return all_articles
    
    def contributors(self):
        all_authors=[authors for authors in Author.all if Author.name==Magazine.name  ]
        return all_authors
    
    def article_titles(self):
        article_titles=[all_titles for all_titles in Article.all if Article.magazine==self.name]
        return article_titles.name

    def contributing_authors(self):
        matching_authors=[]
        matching_authors2=[]
        if Article.magazine==self.name:
            matching_authors.append(Article.author)
        for a in range(len(matching_authors)):
            if matching_authors.count(matching_authors[a]>2):
                matching_authors2.append(matching_authors[a])
        return matching_authors2    
    
    
class Author:
    
    def __init__(self,name):
       if  isinstance(name,str) and 1<=len(name) :
              self.name=name
       else :raise ValueError("Name must be a valid string of length greater than zero")
       Author.all=[]
       Author.all.append(self)
   
    def articles(self):
        my_articles=[articles for articles in Article.all if Article.author==self ]
        return my_articles
    
    def  magazines(self):
        my_magazines=[magazines for magazines in Magazine.all if Magazine.authors==self]
        return my_magazines
    
    def add_article(self,magazine,title):
        Article.title=title
        Article.magazine=magazine
        Article.author=Author(self) 
        Article.all.append(self)
        Magazine.authors.append(self)

    
    def topic_areas(self):
        contributed_articles=[]
        if Magazine.name==self:
            contributed_articles.append(Magazine.category)
        else :return None

my_magazine=Magazine("Sta","ld")
print(my_magazine.name,my_magazine.category)


 

     