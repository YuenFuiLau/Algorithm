def moveUp(pw,digit):

    
    if pw[digit] == "9":

        pw = pw[:digit] + "0" + pw[digit+1:]

    else:

        pw = pw[:digit] + chr( ord(pw[digit]) + 1 ) + pw[digit+1:]

    return pw
    

def moveDown(pw,digit):


    if pw[digit] == "0" :

        pw = pw[:digit] + "9" + pw[digit+1:]

    else:

        pw = pw[:digit] + chr( ord(pw[digit]) - 1 ) + pw[digit+1:]

    return pw


#dead:List , target:List
def unlock(dead,target):

    q= ["0"*len(target)]
    visited = ["0"*len(target)]

    count = 0

    while len(q) != 0:

        for j in range(len(q)):

            trial = q.pop(0)

            if trial == target:

                return count

            if trial in dead:

                continue

            for i in range(len(target)):

                up = moveUp(trial,i)


                if (up not in visited):

                    q.append(up)
                    visited.append(up)


                down = moveDown(trial,i)


                if (down not in visited):

                    q.append(down)
                    visited.append(down)
                    
        
        count += 1

    
    return "Fail to unlock"


dead = [ "0201","0101","0102","1212","2002" ]
target = "0202"

ans = unlock(dead,target)

#------------------------------------------------

dead = [ "8887","8889","8878","8898","8788","8988","7888","9888" ]
target = "8888"

#Notice:pop func change index
for trial in dead:

    tmp = dead.pop(0)

    print("Trial:",trial,"Tmp:",tmp)

#---------------------------------------------------
    
dead = [ "8888" ]
target = "0009"



