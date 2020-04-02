def PassManyVarsWithKeyword(name,**data):
    for keyword,val in data.items():
        print(keyword,val)

PassManyVarsWithKeyword('mohanad',age=34,Gender='Male',Location='Damascus')