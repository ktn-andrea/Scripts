#!/usr/bin/env python3

MELY, MAGAS, VEGYES, SEMMILYEN = range(4)


MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'

def hangrend(words):
    result = []
    for word in words:
        mghk = 0
        mely = 0
        magas = 0
        for i in word:
            if i in MELY_MGHK:
                mghk += 1
                mely += 1
            elif i in MAGAS_MGHK:
                mghk += 1
                magas +=1
        if mely == mghk:
            res = "mely"
        elif magas == mghk:
            res = "magas"
        elif mghk == 0:
            res = "semmilyen"
        else:
            res = "vegyes"
        result.append((word, res))
    return result


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély"]
    result = hangrend(words)
    #print(result)
    for i in range(len(result)):
        print("{0} --> {1}".format(result[i][0], result[i][1]))
        


#############################################################################

if __name__ == "__main__":
    main()
