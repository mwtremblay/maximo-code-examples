#
# Send an email using a comm template with Maximo Automation Scripting
#
# Object: SR
#

from psdi.mbo import MboConstants


def sendEmail():
    try:
        clMbo = mbo.createComm()
        clMbo.setValue("TEMPLATEID", "MYTEMPLATE", MboConstants.NOACCESSCHECK)
        clMbo.setValue("SENDTO", mbo.getString("REPORTEDEMAIL"), MboConstants.NOACCESSCHECK) # assuming you have a relationship called reportedemail
        clMbo.sendMessage()
    except:
        clMbo.setValue("ISSENDFAIL", True, MboConstants.NOACCESSCHECK)

sendEmail()