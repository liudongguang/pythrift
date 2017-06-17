# _*_ coding:utf-8 _*_
__auther__='刘东光'

from py.thrift.generated import ttypes

class PersonServiceImpl:
    def getPersionByUsername(self,username):
        print "got client parm:"+username
        person=ttypes.Persion()
        person.username=username
        person.age=20
        person.married=False
        return person

    def savePersion(self,person):
        print 'got client param:'
        print person.username
        print person.age
        print person.married
