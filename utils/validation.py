def validate_add(a,b):
    x=a.data
    y=b.data
    if len(x)==len(y):#row check
        if len(x[0])==len(y[0]):#col check
            return True
        else:
            print("xxx--- From validate_add ---xxx")
            print("xxx--- No.Columns aren't matching ---xxx")
            return False     
    else:
        print("xxx--- From validate_add ---xxx")
        print("xxx--- No.Rows aren't matching ---xxx")
        return False