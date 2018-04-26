def passCheck( pw ):
    low = [ x for x in pw if x.islower() ]
    up = [ x for x in pw if x.isupper() ]
    num = [ x for x in pw if x.isdigit() ]
    if len(low) > 0 and len(up) > 0 and len(num) > 0 :
        print( "Password has at least one lower case letter, one upper case letter, and one number" )
    else:
        print( "Password does not have at least one lower case letter, one upper case letter, and one number" )

#passCheck( "dragonfruit" )
#passCheck( "passCheck" )
#passCheck( "wOwg00dpa$$word" )

def passStrength( pw ):
    low = [ x for x in pw if x.islower() ]
    up = [ x for x in pw if x.isupper() ]
    num = [ x for x in pw if x.isdigit() ]
    other = [ x for x in pw if not x.islower() and not x.isupper() and not x.isdigit() ]

    if len(low) > 1 and len(up) > 1 and len(num) > 1  and len(other) > 0:
        return 10
    elif len(low) > 0 and len(up) > 0 and len(num) > 0  and len(other) > 0:
        return 9
    elif len(low) > 1 and len(up) > 1 and len(other) > 0:
        return 8
    elif len(low) > 0 and len(up) > 0 and len(other) > 0:
            return 7
    elif (len(low) > 1 or len(up) > 1) and len(num) > 1 and len(other) > 0:
        return 6
    elif (len(low) > 0 or len(up) > 0) and len(num) > 0 and len(other) > 0:
        return 5
    elif len(low) > 1 and len(up) > 1 and len(num) > 1:
        return 4
    elif len(low) > 0 and len(up) > 0 and len(num) > 0:
        return 3
    elif (len(low) > 0 or len(up) > 0) and len(num) > 0:
        return 2
    else:
        return 1

print( passStrength("b00gie") )
print( passStrength("B00gie") )
print( passStrength("Pa$$w0rdsarehard") )
print( passStrength("Pa$$w0rdsar3harD") )
