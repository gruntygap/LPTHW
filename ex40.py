def apple():
    print "I AM APPLES!"

tangerine = "Living reflection of a dream"


class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I am CLASSY APPLES!"

thing = MyStuff()
thing.apple()
print thing.tangerine