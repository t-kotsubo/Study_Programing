def test(w, *args, **kwargs):
    print(w)

    for i in args:
        print(i, end=",")
    print()
    for j in kwargs:
        print(kwargs[j], end=",")


test("w", "args1", "args2", "args3", kwargs1="kw1", kwargs2="kw2", kwargs3="kw3")      


