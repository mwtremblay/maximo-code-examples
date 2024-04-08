#
# Set the list for an attributes Select Value using Maximo Automation Scripting
#
# Required: Create a relationship on your object to define your list contents
# Create this script with a attribute level launch point


def setMyList():
    list = mbo.getMboSet("LISTRELATIONSHIP")
    listMboSet = list

# If you only want to set the list for the list tab and dialogs, use mbo.isZombie()

def setMyListZombie():
    if mbo.isZombie():
        list = mbo.getMboSet("LISTRELATIONSHIP")
        listMboSet = list

setMyList()