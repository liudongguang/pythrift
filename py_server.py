# _*_ coding:utf-8 _*_
__auther__='刘东光'

from py.thrift.generated import PersionService
from PersonServiceImpl import PersonServiceImpl

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer


try:
    personServiceHandler=PersonServiceImpl()
    processor=PersionService.Processor(personServiceHandler)

    serverSocket=TSocket.TServerSocket(host='127.0.0.1',port=8899)
    transportFactory=TTransport.TFramedTransportFactory()
    protocolFactory=TCompactProtocol.TCompactProtocolFactory()

    server=TServer.TSimpleServer(processor,serverSocket,transportFactory,protocolFactory)
    server.serve()



except Thrift.TException, tx:
    print '%s' % tx.message