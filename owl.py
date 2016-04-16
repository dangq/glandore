from rdflib import ConjunctiveGraph, Namespace, exceptions

from rdflib import URIRef, RDFS, RDF, BNode

import OWL

class OntoInspector(object):

    """Class that includes methods for querying an RDFS/OWL ontology"""

    def __init__(self, uri, language=""):
        super(OntoInspector, self).__init__()

        self.rdfGraph = ConjunctiveGraph()
        try:
            self.rdfGraph.parse(uri, format="xml")
        except:
            try:
                self.rdfGraph.parse(uri, format="n3")
            except:
                raise exceptions.Error("Could not parse the file! Is it a valid RDF/OWL ontology?")

        finally:
            # let's cache some useful info for faster access
            self.baseURI = self.get_OntologyURI() or uri
            self.allclasses = self.__getAllClasses(classPredicate)
            self.toplayer = self.__getTopclasses()
            self.tree = self.__getTree()


    def get_OntologyURI(self, ....):
        # todo
        pass

    def __getAllClasses(self, ....):
        # todo
        pass


    def __getTopclasses(self, ....):
        pass


    def __getTree(self, ....):
        # todo
        pass