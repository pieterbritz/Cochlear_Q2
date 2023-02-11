import pytest
import linkedList as llist

thelist = llist.SLinkedList()

@pytest.fixture(scope='session')
def init_linkedlist():
    thelist.AddToEnd("Alfa Romeo") 
    thelist.AddToEnd("Audi") 
    thelist.AddToEnd("BMW") 
    thelist.AddToEnd("Bentley") 
    thelist.AddToEnd("Buick") 
    thelist.AddToEnd("Chevrolet") 
    thelist.AddToEnd("Chrysler") 
    thelist.AddToEnd("Dodge") 
    thelist.AddToEnd("Ford") 
    thelist.AddToEnd("Honda")
#    thelist.PrintList()

def test_PrintListLength(init_linkedlist):
    print("The total number of nodes in the list is: %d" % thelist.CalculateNumberOfNodes() )
    assert thelist.CalculateNumberOfNodes() == 10
    
def test_DeleteTheBuick(init_linkedlist):
    assert thelist.CalculateNumberOfNodes() == 10
    thelist.DeleteNode("Buick")
    thelist.PrintList()
    assert thelist.CalculateNumberOfNodes() == 9

def test_PrintListInReverse(init_linkedlist):
    print("Normal list car models:")
    thelist.PrintList()
    print("List car models in reverse:")
    thelist.PrintListInReverse()