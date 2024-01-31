



from ast import List
from enum import Enum



###################### the two types of the internally/externally structured nodes enumerators, or not defined as a null placeholder 

class NodeType(Enum):
    NotDefined = 0
    InternallyStructuredNode = 1
    ExternallyStructuredNode = 2
    




###################### the base node of the hypertree's two variants of externally/internally strucructyured nodes
class BaseHyperNode:
    """
    The building block of the graph of the HyperTree knowledge represntation of any concept 
    """
    

    def __init__(self):
        """
        the default initializer of the base node's attributes:
        
            "empity" if the node contains pathes or not,
            "parent" the single parent node of this node
            "childern" the list of the childern nodes of this node
        """
        self.empity = True
        self.parent = None ###BaseHyperNode()
        self.childern = None ###List(BaseHyperNode())
        self.nodeType = NodeType.NotDefined
        


    ######### set or get the parent of this node
    def Parent(self, aNode = None):
        if aNode == None:
            return self.parent
        
        self.parent = aNode
        
    

    