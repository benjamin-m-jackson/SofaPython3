"""
           Scene components
           -----------------------

           .. autosummary::
               :toctree: _autosummary
           
               Sofa.Core.Controller
               Sofa.Core.ForceField
               Sofa.Core.Data
               Sofa.Core.Node
               Sofa.Core.BaseObject
       """

from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
__all__  = [
"Base",
"BaseCamera",
"BaseContext",
"BaseNode",
"BaseObject",
"Context",
"Controller",
"Data",
"DataContainer",
"DataContainerContextManager",
"DataDict",
"DataDictIterator",
"ForceField",
"Node",
"NodeIterator"
]
class Base():
    """Sofa.Core.Base is the root of the Sofa Hierarhcy

                                      """
    def __getattr__(self, arg0: str) -> 'object': ...
    def __setattr__(self, arg0: str, arg1: object) -> 'None': ...
    @overload
    def addData(self, name: str, value: object, help: object, group: object, type: object) -> 'None': 
        pass
    @overload
    def addData(self, arg0: object) -> 'None': ...
    def findData(self, arg0: str) -> 'object': ...
    def findLink(self, arg0: str) -> 'object': ...
    def getClass(self) -> 'object': ...
    def getData(self, arg0: str) -> 'object': ...
    def getDataFields(self) -> 'object': ...
    def getLinks(self) -> 'object': ...
    def getName(self) -> 'str': ...
    @overload
    def setName(self, arg0: str) -> 'None': 
        pass
    @overload
    def setName(self, arg0: str, arg1: int) -> 'None': ...
    pass
class BaseCamera():
    def __init__(self, arg0: object) -> 'None': 
        """
:rtype: Sofa.Core.BaseCamera
"""
    def getModelViewMatrix(self) -> 'object': ...
    def getProjectionMatrix(self) -> 'object': ...
    pass
class BaseContext(Base):
    def __getattr__(self, arg0: str) -> 'object': ...
    def __setattr__(self, arg0: str, arg1: object) -> 'None': ...
    @overload
    def addData(self, name: str, value: object, help: object, group: object, type: object) -> 'None': 
        pass
    @overload
    def addData(self, arg0: object) -> 'None': ...
    def findData(self, arg0: str) -> 'object': ...
    def findLink(self, arg0: str) -> 'object': ...
    def getClass(self) -> 'object': ...
    def getData(self, arg0: str) -> 'object': ...
    def getDataFields(self) -> 'object': ...
    def getLinks(self) -> 'object': ...
    def getName(self) -> 'str': ...
    @overload
    def setName(self, arg0: str) -> 'None': 
        pass
    @overload
    def setName(self, arg0: str, arg1: int) -> 'None': ...
    pass
class BaseNode(Base):
    def __getattr__(self, arg0: str) -> 'object': ...
    def __setattr__(self, arg0: str, arg1: object) -> 'None': ...
    @overload
    def addData(self, name: str, value: object, help: object, group: object, type: object) -> 'None': 
        pass
    @overload
    def addData(self, arg0: object) -> 'None': ...
    def findData(self, arg0: str) -> 'object': ...
    def findLink(self, arg0: str) -> 'object': ...
    def getClass(self) -> 'object': ...
    def getData(self, arg0: str) -> 'object': ...
    def getDataFields(self) -> 'object': ...
    def getLinks(self) -> 'object': ...
    def getName(self) -> 'str': ...
    @overload
    def setName(self, arg0: str) -> 'None': 
        pass
    @overload
    def setName(self, arg0: str, arg1: int) -> 'None': ...
    pass
class BaseObject(Base):
    def __getattr__(self, arg0: str) -> 'object': ...
    def __getitem__(self, arg0: str) -> 'object': ...
    def __setattr__(self, arg0: str, arg1: object) -> 'None': ...
    @overload
    def addData(self, name: str, value: object, help: object, group: object, type: object) -> 'None': 
        pass
    @overload
    def addData(self, arg0: object) -> 'None': ...
    def findData(self, arg0: str) -> 'object': ...
    def findLink(self, arg0: str) -> 'object': ...
    def getClass(self) -> 'object': ...
    def getData(self, arg0: str) -> 'object': ...
    def getDataFields(self) -> 'object': ...
    def getLink(self) -> 'str': ...
    def getLinks(self) -> 'object': ...
    def getName(self) -> 'str': ...
    def getPathName(self) -> 'str': ...
    def init(self) -> 'None': ...
    def reinit(self) -> 'None': ...
    @overload
    def setName(self, arg0: str) -> 'None': 
        pass
    @overload
    def setName(self, arg0: str, arg1: int) -> 'None': ...
    pass
class Context(BaseContext, Base):
    def __getattr__(self, arg0: str) -> 'object': ...
    def __setattr__(self, arg0: str, arg1: object) -> 'None': ...
    @overload
    def addData(self, name: str, value: object, help: object, group: object, type: object) -> 'None': 
        pass
    @overload
    def addData(self, arg0: object) -> 'None': ...
    def findData(self, arg0: str) -> 'object': ...
    def findLink(self, arg0: str) -> 'object': ...
    def getClass(self) -> 'object': ...
    def getData(self, arg0: str) -> 'object': ...
    def getDataFields(self) -> 'object': ...
    def getLinks(self) -> 'object': ...
    def getName(self) -> 'str': ...
    @overload
    def setName(self, arg0: str) -> 'None': 
        pass
    @overload
    def setName(self, arg0: str, arg1: int) -> 'None': ...
    pass
class Controller(BaseObject, Base):
    """THIS IS A TEST ROOOOOOOOOOOOOOO
    
    .. autoclass:: 
            :members: addData findData findLink
            
         
    """
    def __getattr__(self, arg0: str) -> 'object': ...
    def __getitem__(self, arg0: str) -> 'object': ...
    def __init__(self, *args, **kwargs) -> 'None': ...
    def __setattr__(self, arg0: str, arg1: object) -> 'None': ...
    @overload
    def addData(self, name: str, value: object, help: object, group: object, type: object) -> 'None': 
        """ADD A NEW DATA FIELD"""
        pass
    @overload
    def addData(self, arg0: object) -> 'None': ...
    def findData(self, arg0: str) -> 'object': ...
    def findLink(self, arg0: str) -> 'object': 
        """ADD A NEW DATA FIELD"""
        pass    
    def getClass(self) -> 'object': ...
    def getData(self, arg0: str) -> 'object': ...
    def getDataFields(self) -> 'object': ...
    def getLink(self) -> 'str': ...
    def getLinks(self) -> 'object': ...
    def getName(self) -> 'str': ...
    def getPathName(self) -> 'str': ...
    def init(self) -> 'None': ...
    def reinit(self) -> 'None': ...
    @overload
    def setName(self, arg0: str) -> 'None': 
        pass
    @overload
    def setName(self, arg0: str, arg1: int) -> 'None': ...
    pass
class Data():
    def __getattr__(self, arg0: str) -> 'object': ...
    def __repr__(self) -> 'str': ...
    def __setattr__(self, arg0: str, arg1: object) -> 'None': ...
    def __str__(self) -> 'str': ...
    def array(self) -> 'array': ...
    def getCounter(self, arg0: object) -> 'int': ...
    def getHelp(self) -> 'str': ...
    def getLink(self) -> 'str': ...
    def getName(self) -> 'str': ...
    def getOwner(self) -> 'Base': ...
    def getParent(self) -> 'Data': ...
    def getPathName(self) -> 'str': ...
    def setName(self, arg0: str) -> 'None': ...
    def toList(self) -> 'object': ...
    def typeName(self) -> 'str': ...
    def unset(self, arg0: object) -> 'None': ...
    @overload
    def writeableArray(self, arg0: object) -> 'object': 
        pass
    @overload
    def writeableArray(self) -> 'object': ...
    pass
class DataContainer(Data):
    def __add__(self, arg0: object) -> 'object': ...
    def __getattr__(self, arg0: str) -> 'object': ...
    def __getitem__(self, arg0: object) -> 'object': ...
    def __iadd__(self, arg0: object) -> 'DataContainer': ...
    def __imul__(self, arg0: object) -> 'object': ...
    def __isub__(self, arg0: object) -> 'DataContainer': ...
    def __len__(self) -> 'int': ...
    def __mul__(self, arg0: object) -> 'object': ...
    def __repr__(self) -> 'str': ...
    def __setattr__(self, arg0: str, arg1: object) -> 'None': ...
    @overload
    def __setitem__(self, arg0: tuple, arg1: object) -> 'object': 
        pass
    @overload
    def __setitem__(self, arg0: int, arg1: object) -> 'object': ...
    @overload
    def __setitem__(self, arg0: slice, arg1: object) -> 'object': ...
    def __str__(self) -> 'str': ...
    def __sub__(self, arg0: object) -> 'object': ...
    def apply(self, arg0: object) -> 'None': ...
    def array(self) -> 'array': ...
    def getCounter(self, arg0: object) -> 'int': ...
    def getHelp(self) -> 'str': ...
    def getLink(self) -> 'str': ...
    def getName(self) -> 'str': ...
    def getOwner(self) -> 'Base': ...
    def getParent(self) -> 'Data': ...
    def getPathName(self) -> 'str': ...
    def setName(self, arg0: str) -> 'None': ...
    def toList(self) -> 'object': ...
    def typeName(self) -> 'str': ...
    def unset(self, arg0: object) -> 'None': ...
    @overload
    def writeable(self) -> 'object': 
        pass
    @overload
    def writeable(self, arg0: object) -> 'object': ...
    @overload
    def writeableArray(self, arg0: object) -> 'object': 
        pass
    @overload
    def writeableArray(self) -> 'object': ...
    pass
class DataContainerContextManager():
    def __enter__(self) -> 'object': ...
    def __exit__(self, arg0: object, arg1: object, arg2: object) -> 'None': ...
    pass
class DataDict():
    """DataDict exposes the data of a sofa object in a way similar to a normal python dictionnary.
                           Eg:
                           for k,v in anObject.__data__.items():
                           print("Data name :"+k+" value:" +str(v)))
                           """
    @overload
    def __getitem__(self, arg0: int) -> 'object': 
        pass
    @overload
    def __getitem__(self, arg0: str) -> 'object': ...
    def __iter__(self) -> 'object': ...
    def __len__(self) -> 'int': ...
    def __setitem__(self, arg0: str, arg1: object) -> 'float': ...
    def items(self) -> 'object': ...
    def keys(self) -> 'object': ...
    def values(self) -> 'object': ...
    pass
class DataDictIterator():
    def __iter__(self) -> 'DataDictIterator': ...
    def __next__(self) -> 'object': ...
    pass
class ForceField(BaseObject, Base):
    def __getattr__(self, arg0: str) -> 'object': ...
    def __getitem__(self, arg0: str) -> 'object': ...
    def __init__(self, *args, **kwargs) -> 'None': ...
    def __setattr__(self, arg0: str, arg1: object) -> 'None': ...
    @overload
    def addData(self, name: str, value: object, help: object, group: object, type: object) -> 'None': 
        pass
    @overload
    def addData(self, arg0: object) -> 'None': ...
    def findData(self, arg0: str) -> 'object': ...
    def findLink(self, arg0: str) -> 'object': ...
    def getClass(self) -> 'object': ...
    def getData(self, arg0: str) -> 'object': ...
    def getDataFields(self) -> 'object': ...
    def getLink(self) -> 'str': ...
    def getLinks(self) -> 'object': ...
    def getName(self) -> 'str': ...
    def getPathName(self) -> 'str': ...
    def init(self) -> 'None': ...
    def reinit(self) -> 'None': ...
    @overload
    def setName(self, arg0: str) -> 'None': 
        pass
    @overload
    def setName(self, arg0: str, arg1: int) -> 'None': ...
    pass
class NodeIterator(): ...    
class Node(BaseNode, Context, BaseContext, Base): ...
class Node(BaseNode, Context, BaseContext, Base):
    """
              Node of the scene graph
              ---------------

              .. autoclass:: Sofa.Node
              :members:
              :undoc-members:

              """
    def __getattr__(self, arg0: str) -> 'object': ...
    def __getitem__(self, arg0: str) -> 'object': ...
    @overload
    def __init__(self) -> 'None': 
        pass
    @overload
    def __init__(self, name: str) -> 'None': ...
    def __old_getChild(self, arg0: int) -> 'object': ...
    def __old_getChildren(self) -> 'list': ...
    def __setattr__(self, arg0: str, arg1: object) -> 'None': ...
    @overload
    def addChild(self, arg0: Node) -> 'Node': 
        pass
    @overload
    def addChild(self, arg0: str, **kwargs) -> 'object': ...
    @overload
    def addData(self, name: str, value: object, help: object, group: object, type: object) -> 'None': 
        pass
    @overload
    def addData(self, arg0: object) -> 'None': ...
    @overload
    def addObject(self, arg0: BaseObject) -> 'object': 
        pass
    @overload
    def addObject(self, arg0: str, **kwargs) -> 'object': ...
    def createChild(self, arg0: str, **kwargs) -> 'object': ...
    def createObject(self, arg0: str, **kwargs) -> 'object': ...
    def findData(self, arg0: str) -> 'object': ...
    def findLink(self, arg0: str) -> 'object': ...
    def getChild(self, arg0: str) -> 'object': ...
    def getClass(self) -> 'object': ...
    def getData(self, arg0: str) -> 'object': ...
    def getDataFields(self) -> 'object': ...
    def getLink(self) -> 'str': ...
    def getLinks(self) -> 'object': ...
    def getName(self) -> 'str': ...
    def getPathName(self) -> 'str': ...
    def getRoot(self) -> 'BaseNode': ...
    def init(self) -> 'None': ...
    @overload
    def removeChild(self, arg0: Node) -> 'None': 
        pass
    @overload
    def removeChild(self, arg0: str) -> 'object': ...
    @overload
    def setName(self, arg0: str) -> 'None': 
        pass
    @overload
    def setName(self, arg0: str, arg1: int) -> 'None': ...
    @property
    def children(self) -> NodeIterator:
        """
:type: NodeIterator"""
    @property
    def objects(self) -> NodeIterator:
        """
:type: NodeIterator"""
    @property
    def parents(self) -> NodeIterator:
        """
:type: NodeIterator"""
    pass
class NodeIterator():
    @overload
    def __getitem__(self, arg0: int) -> 'object': 
        pass
    @overload
    def __getitem__(self, arg0: str) -> 'object': ...
    def __iter__(self) -> 'NodeIterator': ...
    def __len__(self) -> 'object': ...
    def __next__(self) -> 'object': ...
    def at(self, arg0: int) -> 'object': ...
    def remove_at(self, arg0: int) -> 'None': ...
    pass
