class Magazine:
    _all_magazines=[]
    def __init__(self,name,category):
        #Chec if name and categot=ryare vaid strings
        if not isinstance(name,str) or not isinstance(category,str) or len(name)<2 or len(name)>16 or len(category)==0:
            raise ValueError("Name should be a str and btwn 2  and 16 characters and category must be a non empty string")
        self._name=name
        self._category=category
        self._articles=[]#Stores a list of all the articles
        self._all_magazines.append(self)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if not isinstance(value,str) or len(value)<2 or len(value)>16:
            raise ValueError("Name should a string between 2 nd 16")
        self._name=value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self,value):
        if not isinstance(value,str) or len(value)==0:
            raise ValueError("Category should be greater than zero")
        self._category=value

    def articles(self):
        return self._articles
    
    def contributors(self):
        return list(set(article.author for article in self._articles if isinstance(article.author,Author)))
    
    def article_titles(self):
        if not self._articles:
            return None
        return [article for article in self._articles]
    def contributing_authors(self):
        #create a dict with the key being the name of the author
        author_counts={}
        for article in self._articles:
            author=article.author
            if author in author_counts:
                author_counts[author]+=1
            else:author_counts[author]=1
        my_filtered_authors=[author for author,count in author_counts.items() if count>2 and isinstance(author,Author)]
        return my_filtered_authors
    
    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines,key=lambda magazine:len(magazine.articles()))

from author import Author