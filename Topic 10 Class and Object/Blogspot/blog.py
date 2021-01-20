from blogpost import BlogSpot

class Blog:
    def __init__(self):
        self.blogposts = []

    def add(self,blogpost):
        self.blogposts.append(blogpost)
        return self.blogposts

    def delete(self,num):
        for i,v in enumerate(self.blogposts):
            if i + 1 == num:
                self.blogposts.remove(v)

    def update(self,num,BlogSpot):
        for i,v in enumerate(self.blogposts):
            if i + 1 == num:
                self.blogposts[i] == BlogSpot

    def get_blogpost(self):
        return self.blogposts