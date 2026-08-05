def validate_add(a,b):
    x=a.data
    y=b.data
    if len(x)==len(y):
        if len(x[0])==len(y[0]):
            return True
        else:
            print("xxx--- From validate_add ---xxx")
            print("xxx--- No.Columns aren't matching ---xxx")
            return False     
    else:
        print("xxx--- From validate_add ---xxx")
        print("xxx--- No.Rows aren't matching ---xxx")
        return False


def validate_multi(a,b):
    x=a.data
    y=b.data
    if (len(x)==len(y[0])) & (len(x[0])==len(y)):
        return True
    else:
        print(f"xxx--- From validate_multi ---xxx")
        print(f"xxx--- [A](ixj) != [B](jxi) ---xxx")