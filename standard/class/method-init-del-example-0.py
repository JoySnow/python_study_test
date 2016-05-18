# encoding:utf8

class NewClass(object):
    num_count = 0 # 所有的实例都共享此变量，即不单独为每个实例分配
    def __init__(self,name):
        self.name = name
        self.__class__.num_count += 1
        #NewClass.num_count += 1
        print name,NewClass.num_count
    def __del__(self):
#        NewClass.num_count -= 1
#        print "Del",self.name,NewClass.num_count
        self.__class__.num_count -= 1
        print "Del",self.name,self.__class__.num_count

    def test():
        print "aa"

aa = NewClass("Hello")
bb = NewClass("World")
cc = NewClass("aaaa")


print "Over"
