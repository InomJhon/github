t= {"a": 1, "b": 2, "c": 3, "d": 3}
d = {"t":3}

for k,v in t.items():
    if v not in d:
      print(v)



print('d>>>>', d)
