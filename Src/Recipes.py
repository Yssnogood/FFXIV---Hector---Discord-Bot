import json
from math import ceil
from config import Config, DATAID, DATARECIPES

class ItemNotFoundError(Exception):
    """Exception raised when an item is not found in the database."""
    pass

def getId(name, data):
    """Give the id of an item from its name""" 
    for i in data.items():
        if i[1][Config.get_lang()] == name:
            print("Id of ", name, " : ", i[0])
            return i[0]
    raise ItemNotFoundError(f"Item with name '{name}' not found in the database.")

def getName(id, data):
    """Give the name of an id"""
    for i in data.keys():
        if int(i) == id:
            #print("Name of ", id, " ID : ", data[i]["en"])
            return  data[i][Config.get_lang()]
    raise ItemNotFoundError(f"Item with id '{id}' not found in the database.")

def createListRecipe(dataRecipes):
    """Create a list of ids and amounts needed for crafting an item"""
    listRecipe = []
    for x in range(3, 21):
        listRecipe.append(dataRecipes[str(x)])
    return listRecipe

def findRecipe(id, dataRecipes):
    """Find the corresponding recipe of an id given"""
    for i in range(3, len(dataRecipes)):
        
        if int(id) == int(dataRecipes[i][str(3)]):
            #print(dataRecipes[i][str(3)])
            return createListRecipe(dataRecipes[i])
    return []
        
def listIdToName(listId, dataItems):
    """Change ids items to items names"""
    listName = []
    for x in range(0, len(listId)):
        if x%2 == 0 and listId[x] > 0:
            listName.append(getName(listId[x], dataItems))
        elif listId[x] >0 :
            listName.append(listId[x])
    return listName

def MultipleListIdToName(listId, dataItems):

    listName = []
    for listsId in listId:
        subList = []
        for x in range (0, len(listsId)):
            if x%2 == 0 and listsId[x]>0:
                subList.append(getName(listsId[x], dataItems))
            elif listsId[x]>0:
                subList.append(listsId[x])
        listName.append(subList)
    return listName



def multipleCraft(listRecipe, howMany=1):
    """"""
    multipleCraftList = []
    for x in range(0, len(listRecipe)):
        if x%2 != 0:
            multipleCraftList.append(listRecipe[x]*howMany)
        else:
            multipleCraftList.append(listRecipe[x])
    return multipleCraftList

def recipeWithSubFromName(name, howmany=1):

    try:
        id = int(getId(name, DATAID))
    except ItemNotFoundError as e:
        print(e)
        return []
    
    recipes = findRecipeWithSubRecipe(id, DATARECIPES)
    finalRecipe = multipleCraft(recipes[0], howmany)
    finalSubRecipe = recipes[1]
    for x in range(2, len(finalRecipe),2):
        for y in range(0, len(finalSubRecipe)):
            for z in range(1, len(finalSubRecipe[y]),2):
                if finalRecipe[x] == finalSubRecipe[y][0] and finalSubRecipe[y][z] >0 :
                    finalSubRecipe[y] = multipleCraft(finalSubRecipe[y], ceil(finalRecipe[x+1]/finalSubRecipe[y][z]) )
                    break

    return [listIdToName(finalRecipe,DATAID), MultipleListIdToName(finalSubRecipe, DATAID) ]

def recipeFromName(name, howMany=1):
    try:
        id = int(getId(name, DATAID))
    except ItemNotFoundError as e:
        print(e)
        return []
    return multipleCraft(listIdToName(findRecipe(id, DATARECIPES), DATAID),howMany)

def recipeFromId(id, howMany=1):
    return multipleCraft(listIdToName(findRecipe(id, DATARECIPES), DATAID),howMany)

def findRecipeWithSubRecipe(id, dataRecipes):
    """Find the corresponding recipe of an id given"""
    
    for i in range(3, len(dataRecipes)):
        if int(id) == int(dataRecipes[i][str(3)]):
            baseRecipe= createListRecipe(dataRecipes[i])
    subRecipes = []
    for id in baseRecipe[2:14:2]:
        if id != None and id != 0:
            tmp = findRecipe(id, dataRecipes)
            if len(tmp)>0:
                subRecipes.append(tmp)
    return [baseRecipe, subRecipes]


def affichage(name, howMany=1):
    recipePrint=recipeFromName(name, howMany)
    print("Ingredient(s) for ", howMany, "craft(s) of : ", name)
    print("================================================================")
    for x in range(2,len(recipePrint),2):
        print(recipePrint[x], " : ", recipePrint[x+1] )
    print("================================================================")
    print("You'll get : ",recipePrint[1]," of ", recipePrint[0])
