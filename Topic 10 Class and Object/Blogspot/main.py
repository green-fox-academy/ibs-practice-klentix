from blog import Blog
from blogpost import BlogSpot


post1 = BlogSpot('John Doe','Lorem Ipsum','Lorem ipsum dolor sit amet.','2000.05.04')
post2 = BlogSpot("Tim Urban","Wait but why", "A popular long-form, stick-figure-illustrated blog about almost everything.", "2010.10.10.")
post3 = BlogSpot("William Turton","One Engineer Is Trying to Get IBM to Reckon With Trump", "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.", "2017.03.28.")


blog = Blog()
blog.add(post1)
blog.add(post2)
blog.add(post3)

print(len(blog.blogposts))

blog.delete(3)
print(len(blog.blogposts))

blog.update(1,'blog new')
print(len(blog.blogposts))