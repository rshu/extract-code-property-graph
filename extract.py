from neo4j import __version__ as neo4j_version
from neo4j import GraphDatabase
from py2neo import Graph
import py2neo
import pandas as pd


class Neo4jConnection:

    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)

    def close(self):
        if self.__driver is not None:
            self.__driver.close()

    def query(self, query, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try:
            session = self.__driver.session(database=db) if db is not None else self.__driver.session()
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally:
            if session is not None:
                session.close()
        return response


if __name__ == "__main__":
    print(neo4j_version)

    driver = GraphDatabase.driver(uri="neo4j://localhost:7687", auth=("neo4j", "password"), max_connection_lifetime=1000)
    session = driver.session()
    result = session.run("MATCH p=()-[r:ARGUMENTS]->() RETURN p")
    names = [record["p"] for record in result]
    # print(names)
    # print(type(names))
    for r in names:
        print(type(r))
        print(r)
        print()
    session.close()
    driver.close()


    # # connect to neo4j database
    # # requires the url, the username and the password during the initialization
    # conn = Neo4jConnection(uri="neo4j://localhost:7687", user="neo4j", pwd="password")
    # # conn.query("CREATE OR REPLACE DATABASE coradb")
    #
    # query_string = '''
    # MATCH p=()-[r:ARGUMENTS]->() RETURN p LIMIT 25
    # '''
    # response = conn.query(query_string, db='neo4j')
    # print(type(response))
    # print(len(response))
    # for r in response:
    #     print(type(r))
    #     print(r)
    #     print()

    # # dtf_data = DataFrame([dict(_) for _ in conn.query(query_string, db='neo4j')])
    # # # print(dtf_data.sample(10))
    # # print(dtf_data)
    # # conn.close()
    #
    # graph = py2neo.Graph(bolt=True, host='localhost', user='neo4j', password='password')
    # query_string = '''
    # MATCH p=()-[r:ARGUMENTS]->() RETURN p
    # '''
    # print(graph.run(query_string))
    #
    # df = graph.run(query_string).to_data_frame()
    # print(df)
    # print(df.head())
