#
# Add user to a security group using Maximo Automation Scripting
#
# Object: MAXUSER
#

from psdi.mbo import MboConstants

def addUserToGroup():
    try:
        groupUserSet = mbo.getMboSet("GROUPUSER")
        groupUser = groupUserSet.add()
        groupUser.setValue("USERID", mbo.getString("USERID"), MboConstants.NOACCESSCHECK)
        groupUser.setValue("GROUPNAME", "MYSECURITYGROUP", MboConstants.NOACCESSCHECK)
    finally:
        groupUserSet.close()

addUserToGroup()