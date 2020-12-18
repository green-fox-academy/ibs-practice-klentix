class PostIt:
        background = ''
        text = ''
        text_color = ''

post_it1 = PostIt()
post_it1.background = 'orange'
post_it1.text = 'Idea 1'
post_it1.text_color = 'blue'

post_it2 = PostIt()
post_it2.background = 'pink'
post_it2.text = 'Awesome'
post_it2.text_color = 'black'

post_it3 = PostIt()
post_it3.background = 'yellow'
post_it3.text = 'Superb!'
post_it3.text_color = 'yellow'


print('post it 1: ' + '\n Background: ' + post_it1.background + '\n Text: ' +post_it1.text + '\n Text Color: ' +post_it1.text_color)
print('post it 2: ' + '\n Background: ' + post_it2.background + '\n Text: ' +post_it2.text + '\n Text Color: ' +post_it2.text_color)
print('post it 3: ' + '\n Background: ' + post_it3.background + '\n Text: ' +post_it3.text + '\n Text Color: ' +post_it3.text_color)