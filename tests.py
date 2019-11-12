from game import getUniverse



def ifThereIsAUniverse():
    assert getUniverse()!=None

def ifThereIsACellInUniverse():
    assert getUniverse().getCellAt(0, 0) != None

def ifASingleCellIsThereInUniverse():
    assert getUniverse([[0,1]]).getCellAt(0, 1) == True

if __name__ == "__main__":
    ifThereIsAUniverse()
    ifThereIsACellInUniverse()
    ifASingleCellIsThereInUniverse()
    print("Everything passed")
