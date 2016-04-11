
class Countdown(object):

    stop_flag = 2
    counters = [5, 4, 3]

    def count_1(self):
        if self.counters[0]:
            print 'self.count_1: ', self.counters[0], '...'
            self.counters[0] -= 1
            reactor.callLater(1, self.count_1)
        elif self.stop_flag == 0:
            print "self.count_1: What's going on here ?"
            reactor.stop()
        else:
            print 'self.count_1: +++', self.stop_flag
            self.stop_flag -= 1
            print 'self.count_1: ---', self.stop_flag

    def count_2(self):
        if self.counters[1]:
            print 'self.count_2: >>', self.counters[1], '...'
            self.counters[1] -= 1
            reactor.callLater(2, self.count_2)
        elif self.stop_flag == 0:
            print "self.count_2: What's going on here ?"
            reactor.stop()
        else:
            print 'self.count_2: +++', self.stop_flag
            self.stop_flag -= 1
            print 'self.count_2: ---', self.stop_flag

    def count_3(self):
        if self.counters[2]:
            print 'self.count_3: >>>>', self.counters[2], '...'
            self.counters[2] -= 1
            reactor.callLater(5, self.count_3)
        elif self.stop_flag == 0:
            print "self.count_3: What's going on here ?"
            reactor.stop()
        else:
            print 'self.count_3: +++', self.stop_flag
            self.stop_flag -= 1
            print 'self.count_3: ---', self.stop_flag


from twisted.internet import reactor

cnt = Countdown()

reactor.callWhenRunning(cnt.count_1)
reactor.callWhenRunning(cnt.count_2)
reactor.callWhenRunning(cnt.count_3)

print 'Start!'
reactor.run()
#reactor.stop()
print 'Stop!'
