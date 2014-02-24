from environment import *
from agent import *
from package import *


#            A
#          |  |
#          | 2|
#          |  |
#     -----    ------------
#    B  3   C   3  D    4  E
#     ---    -----    -----
#        |  |     |  |
#        | 5|     | 4|
#        |  |       F 
#        |  |   
#     ---    -----
#    G  3  H   4   I
#     ------------
#        

gr1 = Graph(['A','B','C','D','E','F','G','H','I'],
            [('A','C',2),('B','C',3),('C','D',3),('D','E',4),('D','F',4),('C','H',5),('G','H',3),('H','I',4)],
            ['A','B','E','F','G','I'])

agent = Agent(gr1,'A')
environment = Environment(gr1,agent) 
environment.addPackage(Package('B','F', 2, 'p2102'),0)
environment.addPackage(Package('B','A', 2, 'p5431'),0)
environment.addPackage(Package('B','A', 3, 'p1873'),7)
environment.addPackage(Package('F','B', 3, 'p2317'),10)
environment.addPackage(Package('G','E', 3, 'p2312'),10)
environment.addPackage(Package('I','G', 3, 'p2232'),10)
environment.addPackage(Package('F','A', 2, 'p2111'),7)
environment.addPackage(Package('I','B', 2, 'p2000'),0)
environment.addPackage(Package('A','F', 1, 'p2001'),5)
environment.addPackage(Package('G','E', 4, 'p2002'),0)
environment.addPackage(Package('G','E', 3, 'p2003'),0)
environment.addPackage(Package('I','G', 2, 'p2004'),0)
environment.addPackage(Package('A','G', 2, 'p9102'),7)
environment.addPackage(Package('B','I', 2, 'p431'),0)
environment.addPackage(Package('B','F', 3, 'p9873'),5)
environment.addPackage(Package('F','B', 3, 'p9317'),0)
environment.addPackage(Package('G','G', 3, 'p9312'),10)
environment.addPackage(Package('I','E', 3, 'p9232'),10)
environment.addPackage(Package('F','A', 2, 'p21110'),5)
environment.addPackage(Package('I','G', 2, 'p20000'),7)
environment.addPackage(Package('A','B', 1, 'p20010'),0)
environment.addPackage(Package('G','E', 4, 'p20020'),0)
environment.addPackage(Package('G','A', 3, 'p20030'),5)
environment.addPackage(Package('I','B', 2, 'p20040'),0)
environment.addPackage(Package('F','B', 1, 'p1'),0)
environment.addPackage(Package('A','E', 4, 'p2'),7)
environment.addPackage(Package('B','A', 3, 'p3'),0)
environment.addPackage(Package('G','B', 2, 'p4'),5)
environment.addPackage(Package('E','B', 1, 'p5'),0)
environment.addPackage(Package('A','E', 4, 'p6'),0)
environment.addPackage(Package('I','A', 3, 'p7'),10)
environment.addPackage(Package('I','B', 2, 'p8'),5)
environment.addPackage(Package('F','B', 1, 'p9'),7)
environment.addPackage(Package('G','E', 4, 'p21'),10)
environment.addPackage(Package('E','A', 3, 'p31'),0)
environment.addPackage(Package('E','B', 2, 'p41'),5)
environment.addPackage(Package('E','B', 1, 'p51'),0)
environment.addPackage(Package('B','E', 4, 'p61'),0)
environment.addPackage(Package('B','A', 3, 'p71'),0)
environment.addPackage(Package('B','G', 2, 'p81'),5)
environment.addPackage(Package('A','B', 1, 'p188'),7)
environment.addPackage(Package('A','E', 4, 'p288'),0)
environment.addPackage(Package('I','A', 3, 'p388'),5)
environment.addPackage(Package('A','B', 2, 'p488'),7)
environment.addPackage(Package('A','B', 1, 'p588'),7)
environment.addPackage(Package('A','E', 4, 'p688'),7)
environment.addPackage(Package('G','A', 3, 'p788'),5)
environment.addPackage(Package('A','B', 2, 'p888'),7)
environment.addPackage(Package('A','B', 1, 'p988'),5)
environment.addPackage(Package('A','E', 4, 'p218'),7)
environment.addPackage(Package('E','A', 3, 'p318'),0)
environment.addPackage(Package('A','B', 2, 'p418'),5)
environment.addPackage(Package('A','B', 1, 'p518'),0)
environment.addPackage(Package('A','E', 4, 'p618'),10)
environment.addPackage(Package('B','A', 3, 'p718'),10)
environment.addPackage(Package('A','G', 2, 'p818'),450)

environment.run()





