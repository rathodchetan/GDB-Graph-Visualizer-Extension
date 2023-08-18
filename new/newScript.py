import gdb
import json


def graphType1():
    lst = []
    # Variables in C++ file
    var=json.load(open('config.json','r'))
    nodes=var['Node']
    child=var['child']
    val=var['val']

    node_sym = gdb.lookup_symbol("%s" %nodes)[0]
    node_symtab = node_sym.symtab

    if node_sym.is_valid() and node_symtab.is_valid():
        num_nodes = int(gdb.parse_and_eval("%s.size()" %nodes))
        l = []
        for i in range(num_nodes):
            # Value in l = (Node no.) (Node Value) (Node Color [Red/Green]) (Node Shared PTR src) (Node Shared PTR trt)
            l.append((str(i),str(gdb.parse_and_eval("%s[%d].%s" %(nodes,i,val))),str(gdb.parse_and_eval("%s[%d].%s" %(nodes,i,"is_matching"))),str(gdb.parse_and_eval("%s[%d].%s" %(nodes,i,"src"))),str(gdb.parse_and_eval("%s[%d].%s" %(nodes,i,"tgt")))))
            for j in range(gdb.parse_and_eval("%s[%d].%s.size()" %(nodes,i,child))):

                t = (str(gdb.parse_and_eval("%s[%d].%s" %(nodes,i,val))),str(gdb.parse_and_eval("%s[%d].%s[%d]->%s" %(nodes,i,child,j,val))))
                lst.append(t)
    return l, lst

def graphType2():
    lst = []
    # Variables in C++ file
    var=json.load(open('config.json','r'))
    nodes=var['Node']
    child=var['child']
    val=var['val']

    node_sym = gdb.lookup_symbol("%s" %nodes)[0]
    node_symtab = node_sym.symtab

    if node_sym.is_valid() and node_symtab.is_valid():
        num_nodes = int(gdb.parse_and_eval("%s.size()" %nodes))
        l = []
        for i in range(num_nodes):
            # Value in l = (Node no.) (Node Value) (Shared PTR cfg) (Matching block on the opposite side)
            l.append((str(i),str(gdb.parse_and_eval("%s[%d].%s" %(nodes,i,val))),str(gdb.parse_and_eval("%s[%d].%s" %(nodes,i,"cfg"))),str(gdb.parse_and_eval("%s[%d].%s" %(nodes,i,"matching_blks")))))
            for j in range(gdb.parse_and_eval("%s[%d].%s.size()" %(nodes,i,child))):

                t = (str(gdb.parse_and_eval("%s[%d].%s" %(nodes,i,val))),str(gdb.parse_and_eval("%s[%d].%s[%d]->%s" %(nodes,i,child,j,val))))
                lst.append(t)
    return l, lst


def graphType3():
    lst = []
    # Variables in C++ file
    var=json.load(open('config.json','r'))
    nodes=var['Node']
    child=var['child']
    val=var['val']
    color=var['color']
    data=var['data']

    node_sym = gdb.lookup_symbol("%s" %nodes)[0]
    node_symtab = node_sym.symtab

    if node_sym.is_valid() and node_symtab.is_valid():
        num_nodes = int(gdb.parse_and_eval("%s.size()" %nodes))
        l = []
        for i in range(num_nodes):
            
            l.append((str(i),str(gdb.parse_and_eval("%s[%d].%s" %(nodes,i,color))),str(gdb.parse_and_eval("%s[%d].%s" %(nodes,i,data)))))
            
            for j in range(gdb.parse_and_eval("%s[%d].%s.size()" %(nodes,i,child))):

                t = (str(gdb.parse_and_eval("%s[%d].%s" %(nodes,i,val))),str(gdb.parse_and_eval("%s[%d].%s[%d]->%s" %(nodes,i,child,j,val))))
                lst.append(t)
    return l, lst

def graphType4():
    lst = []
    # Variables in C++ file
    var=json.load(open('config.json','r'))
    nodes=var['Node']
    child=var['child']
    val=var['val']

    node_sym = gdb.lookup_symbol("%s" %nodes)[0]
    node_symtab = node_sym.symtab

    if node_sym.is_valid() and node_symtab.is_valid():
        num_nodes = int(gdb.parse_and_eval("%s.size()" %nodes))
        l = []
        for i in range(num_nodes):
            
            for j in range(gdb.parse_and_eval("%s[%d].%s.size()" %(nodes,i,child))):

                t = (str(gdb.parse_and_eval("%s[%d].%s" %(nodes,i,val))),str(gdb.parse_and_eval("%s[%d].%s[%d]->%s" %(nodes,i,child,j,val))))
                lst.append(t)
    return l, lst


def rendergraph(event):
    graphUsed = 0
    try:
        l, lst=graphType1()
        graphUsed=1
    except:
        try:
            l, lst=graphType2()
            graphUsed=2
        except:
            try:
                l, lst=graphType3()
                graphUsed=3
            except:
                l, lst=graphType4()
                graphUsed=4


    file = open('edge.txt','w')
    file1 = open('node.txt','w')
    for i in range(len(lst)):
        lst[i] = " ".join(lst[i])

    file.write("\n".join(lst))
    file.close()

    for i in range(len(l)):
        l[i] = " ".join(l[i])

    file1.write("\n".join(l))
    file1.close()
    print(lst)


gdb.events.stop.connect(rendergraph)