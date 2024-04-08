#
# Report asset downtime from a workorder using Maximo Automation Scripting
#
# Object: WORKORDER
#

from psdi.server import MXServer

def reportDowntime():
    aMboSet = mbo.getMboSet("ASSET")
    if not aMboSet.isEmpty():
        aMbo = aMboSet.getMbo(0)
        aMbo.recordAssetStatusChange(mbo, MXServer.getMXServer().getDate(), "BRKDWN", 0)
        # recordAssetStatusChange(woMbo, changeDate, code, operational)

reportDowntime()