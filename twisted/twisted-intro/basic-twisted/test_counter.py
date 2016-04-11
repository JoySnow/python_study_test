
class Counter(object):

    counter = 5

    def count_1(self):
        self.counter -= 1
        print self.counter

    def count_2(self):
        self.counter -= 1
        print self.counter

    def count_3(self):
        self.counter -= 1
        print self.counter

cnt = Counter()
cnt.count_1()
cnt.count_2()
cnt.count_3()

