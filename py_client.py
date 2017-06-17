# _*_ coding:utf-8 _*_
__auther__='刘东光'

from py.thrift.generated import PersionService
from py.thrift.generated import  ttypes

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

import sys
reload(sys)
sys.setdefaultencoding('utf8')

try:
    tSocket=TSocket.TSocket('127.0.0.1',8899)
    tSocket.setTimeout(600)

    transport=TTransport.TFramedTransport(tSocket)
    protocol=TCompactProtocol.TCompactProtocol(transport)
    client=PersionService.Client(protocol)

    transport.open()

    person=client.getPersionByUsername("张三")

    print person.username
    print person.age
    print person.married

    print '---------'

    newPerson=ttypes.Persion()
    newPerson.username='李四'
    newPerson.age=63
    newPerson.married=True

    client.savePersion(newPerson)

    transport.close()

except Thrift.TException,tx:
    print '%s' % tx.message