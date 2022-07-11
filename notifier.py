import random
import notify2

quote_path = '---your path---'
heart_path = '---your path---'


def sendmessage(title, message):
    notify2.init("hi")
    notice = notify2.Notification(title, message, heart_path)
    notice.show()
    return


# get file liens leght
f = open(quote_path)
max = len(f.readlines())
f.close()

# random int to pick random line
rnd = random.randint(0 , max)

# pick our selected quote
f = open(quote_path)
if rnd == max:
    my_quot = f.readlines()[rnd-1:rnd]
else:
    my_quot = f.readlines()[rnd:rnd+1]
f.close()

# slice our quote
my_quot = str(my_quot)
my_quot = my_quot[2:len(my_quot)-4]

sendmessage('hey :D', my_quot)