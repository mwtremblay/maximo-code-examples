#
# You can call other scripts and pass parameters to them. This can be used to create library scripts to promote code reuse.
#

from java.util import HashMap

def callMyScript():
    params = HashMap()
    params.put("myMbo", mbo)
    service.invokeScript("LIBRARY.MYLIBRARYSCRIPT", params)

callMyScript()