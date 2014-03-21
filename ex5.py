my_name   = "Fernando Castellanos"
my_age    = 32
my_height = 72
my_weight = 170
my_eyes   = 'Light Brown'
my_teeth  = 'White'
my_hair   = 'Brown'

# we can use %r format charater to print, prints whatever it has
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d punds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)