import math
import array


def ispow2(m):
    for i in range(len(m)):
        if (m[i] > 0):
            resultLog = math.log2(m[i])
            if(resultLog.is_integer()):
                print("index",i,"value",m[i])




m = array.array('i',[5,3,5,8])
ispow2(m)