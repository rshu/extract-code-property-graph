from neo4j import __version__ as neo4j_version
from py2neo import Graph
import matplotlib.pyplot as plt
import pandas as pd
import re

if __name__ == "__main__":
    print(neo4j_version)

    # connect to graph database
    graphdb = Graph(scheme="bolt", host="localhost", port=7687, secure=False, auth=('neo4j', 'password'))

    # graphdb.delete_all()

    # print summary statistics
    print(str(graphdb.run("""MATCH (n) RETURN count(n)""").evaluate()) + " nodes")
    print(str(graphdb.run("""MATCH (n:Expression) RETURN count(n)""").evaluate()) + " Expressions")
    print(str(graphdb.run("""MATCH (n:ForEachStatement) RETURN count(n)""").evaluate()) + " ForEachStatement")
    print(str(graphdb.run("""MATCH ()-[r]->() RETURN count(*)""").evaluate()) + " relationships")
    print("")

    # # types of nodes
    # print(graphdb.run("""MATCH (n) RETURN labels(n) AS NodeType, count(n) AS NumberOfNodes""").to_table())
    #
    # # types of relationships (edges)
    # print(graphdb.run(
    #     """MATCH  ()-[r]-() RETURN type(r) AS RelationshipType, count(r) AS NumberOfRelationships""").to_table())

    print(graphdb.run("""MATCH (n:FunctionDeclaration) RETURN (n)""").to_table())
    to_remove_lst = ["Node,", "Statement,", "Declaration,", "Expression,"]

    node_df = graphdb.run("""MATCH (n) RETURN labels(n) AS NodeType, count(n) AS NumberOfNodes""").to_data_frame()
    print(node_df)
    node_df['NodeType'] = node_df['NodeType'].astype(str).str.replace("[", "")
    node_df['NodeType'] = node_df['NodeType'].astype(str).str.replace("]", "")
    node_df['NodeType'] = node_df['NodeType'].astype(str).str.replace("'", "")
    print(node_df)
    node_array = node_df.transpose().values
    n_df = pd.DataFrame(node_array)
    print(n_df)

    relationship_df = graphdb.run(
        """MATCH ()-[r]-() RETURN type(r) AS RelationshipType, count(r) AS NumberOfRelationships""").to_data_frame()
    print(relationship_df)
    print(relationship_df.transpose().values)
    relationship_array = relationship_df.transpose().values
    print("")
    r_df = pd.DataFrame(relationship_array)
    print(r_df)

    df = pd.concat([n_df, r_df], axis=1)
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    print(df)
    df.to_csv('output.csv', index=False)

    # # Summary stats
    # print(graphdb.run("""MATCH ()-[p]-() RETURN type(p) as relationshipType, count(p) AS total""").to_table())

    # driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "password"),
    #                               max_connection_lifetime=1000)
    # session = driver.session()
    #
    # # print summary of sample dataset
    #
    # num_of_nodes = session.run("MATCH (n) RETURN count(n)")
    # count = [record["count(n)"] for record in num_of_nodes]
    # print(count)
    #
    # print(str(session.run("MATCH (n) RETURN count(n)")) + " nodes")
    # print(str(session.run("""MATCH (n:Movie) RETURN count(n)""")) + " movies")
    # print(str(session.run("""MATCH (n:Person) RETURN count(n)""")) + " persons")
    # print(str(session.run("""MATCH ()-[r]->() RETURN count(*)""")) + " relationships")
    # session.close()
    # driver.close()
    #
    #
    # result = session.run("MATCH (n) RETURN count(n)")
    # names = [record["count(n)"] for record in result]
    # # print(names)
    # # print(type(names))
    # for r in names:
    #     print(type(r))
    #     print(r)
    #     print()
    # session.close()
    # driver.close()
    #
    # # # connect to neo4j database
    # # # requires the url, the username and the password during the initialization
    # # conn = Neo4jConnection(uri="neo4j://localhost:7687", user="neo4j", pwd="password")
    # # # conn.query("CREATE OR REPLACE DATABASE coradb")
    # #
    # # query_string = '''
    # # MATCH p=()-[r:ARGUMENTS]->() RETURN p LIMIT 25
    # # '''
    # # response = conn.query(query_string, db='neo4j')
    # # print(type(response))
    # # print(len(response))
    # # for r in response:
    # #     print(type(r))
    # #     print(r)
    # #     print()
    #
    # # # dtf_data = DataFrame([dict(_) for _ in conn.query(query_string, db='neo4j')])
    # # # # print(dtf_data.sample(10))
    # # # print(dtf_data)
    # # # conn.close()
    # #
    # # graph = py2neo.Graph(bolt=True, host='localhost', user='neo4j', password='password')
    # # query_string = '''
    # # MATCH p=()-[r:ARGUMENTS]->() RETURN p
    # # '''
    # # print(graph.run(query_string))
    # #
    # # df = graph.run(query_string).to_data_frame()
    # # print(df)
    # # print(df.head())
