#
# Performant way to loop through an mboset in Maximo Automation Scripting
#


def loopThroughTheSet():
    myMboSet = mbo.getMboSet("MYRELATIONSHIP")

    try:
        myMbo = myMboSet.moveFirst()

        while(myMbo):
            service.log_info("Here is myMbo! " + myMbo.getString("MBOID"))
            myMbo = myMboSet.moveNext() # don't forget this or you'll cause an infinite loop!
    finally:
        myMboSet.close()