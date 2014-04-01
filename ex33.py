# moved the while logic to a method as the study drill suggested
def load_numbers_list(limit):
  i = 0
  while i < limit:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

numbers = []

load_numbers_list(6)

print "The numbers: "

for num in numbers:
  print num
