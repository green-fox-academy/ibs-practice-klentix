class PostIt:

        def __init__(self,background,text,color):
                self.background = background
                self.text = text
                self.text_color = color

post_it1 = PostIt('orange','Idea 1','blue')
print(post_it1.text)

# post_it1 = PostIt('orange','Idea 1','blue')
# post_it2 = PostIt('pink','Awesome','black')
# post_it3 = PostIt('yellow','Superb!','yellow')


#
# print('post it 1: ' + '\n Background: ' + post_it1.background + '\n Text: ' +post_it1.text + '\n Text Color: ' +post_it1.text_color)
# print('post it 2: ' + '\n Background: ' + post_it2.background + '\n Text: ' +post_it2.text + '\n Text Color: ' +post_it2.text_color)
# print('post it 3: ' + '\n Background: ' + post_it3.background + '\n Text: ' +post_it3.text + '\n Text Color: ' +post_it3.text_color)