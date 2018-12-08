from py2neo import Graph
import networkx as nx
import numpy as np


G=nx.Graph()
#graph=Graph("http://church.cs.us.es:7474/db/data",user="neo4j",password="pstorres")


def traversalSimple(host,user,password,query,nombre):

    graph=Graph(host,user=user,password=password)


    #print(query)
    query = str(query)
    if ((query.find('OR' or 'AND' or 'NOT')==-1)):
        query= "match p="+query+"return a, id(a),b,id(b),count(p)"
        print(query)
    else:
        query= "Match (a),(b) where"+query+"return a,id(a),b,id(b)"
        print(query)
    cursor= graph.run(query)

    for c in cursor:
        idNodeA=c[1]
        idNodeB=c[3]
       # G.add_edge(idNodeA,idNodeB,weight=c[4])
        G.add_edge(idNodeA, idNodeB)
        #G.node[idNodeA]['tipoNodo'] = nA
        #G.node[idNodeB]['tipoNodo'] = nB

        for x in c[0]:
            G.node[idNodeA][x] = c[0][x]

        for x in c[2]:
            G.node[idNodeB][x] = c[2][x]
#**************metricas********************

    #****************DEGREE****************
    degreeNode=nx.degree_centrality(G)
    for n in degreeNode:
        G.node[n]['degree']=degreeNode[n]
    #***************************************

        #*************BETWEENNESS***********
    btnessNode=nx.betweenness_centrality(G)
    for n in btnessNode:
        G.node[n]['betweeness']=btnessNode[n]
    #***************************************

    #****************DEGREE****************
    prankNode=nx.pagerank(G)
    for n in btnessNode:
        G.node[n]['pagerank']=prankNode[n]
    #***************************************

    pos = nx.spring_layout(G,dim=2, weight='weight')
    for n in pos:
        G.node[n]['viz']={'position':{'x':pos[n][0],'y':pos[n][1],'z':0.0},'size':10}
        #G.node[n]['viz'] = {'size':10}



    #EXPORTACION A GEPHI

    nx.write_gexf(G,"tesisForm/static/tesisForm/"+ nombre+".gexf",encoding="UTF-8",version='1.2draft')

"""**************************************************************************************************************************************************"""


"""**************************************************************************************************************************************************"""

def namesOfNodes(host,user,password):

    graph=Graph(host,user=user,password=password)
    query2 = "MATCH (n) WITH DISTINCT LABELS(n) AS temp UNWIND temp AS label RETURN distinct label"
    cursor2 = graph.run(query2)
    nombresNodos = []
    for c in cursor2:
        nameNode = c[0]
        nombresNodos.append(nameNode)

    return nombresNodos
"""**************************************************************************************************************************************************"""


def namesOfRelationships(host,user,password):

    graph=Graph(host,user=user,password=password)
    query2 = "MATCH (a)-[r]->(b) RETURN DISTINCT TYPE(r)"
    cursor2 = graph.run(query2)
    nombresRelaciones = []
    for c in cursor2:
        nameNode = c[0]
        nombresRelaciones.append(nameNode)

    return nombresRelaciones
#nodosddd=namesOfNodes('http://178.128.231.142:7474/','neo4j','pstorres')
#rel2=namesOfRelationships('http://178.128.231.142:7474/','neo4j','pstorres')
#print(nodosddd)
#print(rel2)
#<form method="get" action=" {{nombreA}}.gexf">

#-*/-*/-*/-*/*-*/*-/*-/*-/*-/*-/*-/*-/*-/-/*-/PRUEBAS*-/*/-*/-/*-/*-/*--**-*-*-/-*/*-/*-/*-/-/-*/*-/*-/-/


#*********************************************cine*****************************************
#newTraversal('http://localhost:7474/','neo4j','pstorres','Person','Person','-[:ACTED_IN]->(:Movie)<-[:DIRECTED]-(:Person)-[:DIRECTED]->(:Movie)<-[:ACTED_IN]-','TraversalP')
#llnewTraversal('http://localhost:7474/','neo4j','pstorres','Person','Person','-[:PRODUCED]->(:Movie)<-[:ACTED_IN]-','sm')

#traversalC2('http://178.128.231.142:7474/','neo4j','pstorres','Person','Person','-[:ACTED_IN]->(:Movie)<-[:DIRECTED]-(:Person)-[:DIRECTED]->(:Movie)<-[:ACTED_IN]-','Person','Person','-[:PRODUCED]->(:Movie)<-[:ACTED_IN]-','traversal')

#traversalSimple('http://178.128.231.142:7474/','neo4j','pstorres','Person','Person','-[:PRODUCED]->(:Movie)<-[:ACTED_IN]-','TraversalP2')
#traversalC2('http://178.128.231.142:7474/','neo4j','pstorres','Person','Person','-[:PRODUCED]->(:Movie)<-[:ACTED_IN]-','Person','Person','-[:ACTED_IN]->(:Movie)<-[:DIRECTED]-(:Person)-[:DIRECTED]->(:Movie)<-[:ACTED_IN]-','TraversalP')

#*************************************************MÁLAGA*****************************************************************************
#newTraversal('http://localhost:7474/','neo4j','pstorres','Autor','Autor','<-[:tiene_asociado_un_autor]-(:Exposicion)-[:tiene_asociado_un_comisario]->(:Comisario)<-[:tiene_asociado_un_comisario]-(:Exposicion)-[:tiene_asociado_un_autor]->','T1')
#newTraversal('http://localhost:7474/','neo4j','pstorres','Autor','Autor','<-[:tiene_asociado_un_autor]-(:Exposicion)-[:organizada_por_la_entidad]->(:Entidad)<-[:organizada_por_la_entidad]-(:Exposicion)-[:tiene_asociado_un_autor]->','T2')
#newTraversal('http://localhost:7474/','neo4j','pstorres','Pais','Comisario','<-[:tiene_un_pais_de_origen]-(:Autor)<-[:tiene_asociado_un_autor]-(:Exposicion)-[:tiene_asociado_un_comisario]->','T4')
#newTraversal('http://localhost:7474/','neo4j','pstorres','Pais','Entidad','<-[:tiene_un_pais_de_origen]-(:Autor)<-[:tiene_asociado_un_autor]-(:Exposicion)-[:organizada_por_la_entidad]->','T3')


#traversalSimple('http://178.128.231.142:7474/','neo4j','pstorres','Person','Person','Match p=((a:Person)-[:PRODUCED]->(:Movie) <-[:ACTED_IN]-(b:Person)) return a,id(a),b,id(b),count(p)','proyeccionT')


#traversalSimple('http://178.128.231.142:7474/','neo4j','pstorres','(a:Person)-[:WROTE]->(:Movie) <-[:ACTED_IN]-(b:Person)','prueba1')

#traversalSimple('http://178.128.231.142:7474/','neo4j','pstorres','(a:Person)-[:DIRECTED]->(:Movie) <-[:WROTE]-(b:Person) OR (a:Person)-[:PRODUCED]->(:Movie) <-[:ACTED_IN]-(b:Person) ','prueba2')




#nodosddd=namesOfNodes('l','neo4j','pstorres')




