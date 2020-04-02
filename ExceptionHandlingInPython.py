

def div(a,b):
    try:
        print("open connection")
        print(a/b)
    except Exception as e:
        print(e)
    finally:
        print("this statment will excute any way")

div(5,0)