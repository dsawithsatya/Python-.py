def test_case5():
    s={1,2,3,5,6}
    s1={2,5,6,7,1,3}# 
    print(s)
    print()
    print(type(s))
    s.union(s1)
    for i in s:
        print(i)