def rearrange_steps(sets, startat):
    #print sets, startat
    if sets < 8:
        if sets == 3:
            print "2 to -1"
            print "5 to 2"
            print "3 to -3"
            return
        elif sets == 4:
            array = [(startat + 6, startat - 1), (startat + 3, startat + 6), (startat + 0, startat + 3), (startat + 7, startat + 0)]
            for item in array:
                print "%s to %s" % (item[0], item[1])
            return
        elif sets == 5:
            array = [(startat + 8, startat - 1), (startat + 3, startat + 8), (startat + 6, startat + 3), (startat + 0, startat + 6), (startat + 9, startat + 0)]
            for item in array:
                print "%s to %s" % (item[0], item[1])
        elif sets == 6:
            array = [(startat + 10, startat - 1), (startat + 7, startat + 10), (startat + 2, startat + 7), (startat + 6, startat + 2), (startat + 0, startat + 6), (startat + 11, startat + 0)]
            for item in array:
                print "%s to %s" % (item[0], item[1])
        elif sets == 7:
            array = [(startat + 8, startat - 1), (startat + 5, startat + 8), (startat + 12, startat + 5), (startat + 3, startat + 12), (startat + 9, startat + 3), (startat + 0, startat + 9), (startat + 13, startat + 0)]
            for item in array:
                print "%s to %s" % (item[0], item[1])
    else:
        outer_rearrange1(sets, startat)
        rearrange_steps(sets - 4, startat + 4)
        outer_rearrange2(sets, startat)
        return


def outer_rearrange1(sets, startat):
    #print " outer_rearrange1 %s %s" % (sets, startat)
    array = [(startat + (2 * sets) - 2, startat - 1), (startat + 3, startat + (2 * sets) - 2)]
    for item in array:
        print "%s to %s" % (item[0], item[1])
    

def outer_rearrange2(sets, startat):
    #print " outer_rearrange2 %s %s" % (sets, startat)
    array = [(startat + 0, startat + (2 * sets) - 5), (startat + (2 * sets) - 1, startat + 0)]
    for item in array:
        print "%s to %s" % (item[0], item[1])


sets = int(raw_input())
startat = 0
rearrange_steps(sets, startat)
