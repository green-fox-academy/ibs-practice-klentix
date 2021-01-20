from sharpie import Sharpie
from sharpie_set import Sharpieset

green = Sharpie('green',0.5)
red = Sharpie('red',0.3)
black = Sharpie('black', 0.2)

set_of_sharpie = Sharpieset ()

green.use()
black.use()
black.use()
black.use()
black.use()
black.use()
black.use()
black.use()
black.use()




set_of_sharpie.add(green)
set_of_sharpie.add(red)
set_of_sharpie.add(black)
print(set_of_sharpie.count_usuable())
print(set_of_sharpie.remove_trash())
