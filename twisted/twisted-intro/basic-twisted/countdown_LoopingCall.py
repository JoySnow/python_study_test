
class Countdown(object):

    stop_flag = 2
    counters = [5, 4, 3]

    def count_1(self):
        if self.counters[0]:
            print 'self.count_1: ', self.counters[0], '...'
            self.counters[0] -= 1
        else:
            print "loopcall_1 is stoped here ..."
            loopcall_1.stop()
            if self.stop_flag:
                self.stop_flag -= 1
            else:
                reactor.stop()

    def count_2(self):
        if self.counters[1]:
            print 'self.count_2: >>', self.counters[1], '...'
            self.counters[1] -= 1
        else:
            print "loopcall_2 is stoped here ..."
            loopcall_2.stop()
            if self.stop_flag:
                self.stop_flag -= 1
            else:
                reactor.stop()

    def count_3(self):
        if self.counters[2]:
            print 'self.count_3: >>>>', self.counters[2], '...'
            self.counters[2] -= 1
        else:
            print "loopcall_3 is stoped here ..."
            loopcall_3.stop()
            if self.stop_flag:
                self.stop_flag -= 1
            else:
                reactor.stop()


from twisted.internet import reactor
from twisted.internet import task

cnt = Countdown()
loopcall_1 = task.LoopingCall(cnt.count_1)
loopcall_2 = task.LoopingCall(cnt.count_2)
loopcall_3 = task.LoopingCall(cnt.count_3)

loopcall_1.start(1)
loopcall_2.start(2)
loopcall_3.start(5)

#reactor.callWhenRunning(cnt.count_1)
#reactor.callWhenRunning(cnt.count_2)
#reactor.callWhenRunning(cnt.count_3)

print 'Start!'
reactor.run()
#reactor.stop()
print 'Stop!'
