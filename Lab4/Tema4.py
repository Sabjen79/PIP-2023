# Ex 1
def ex1(A, B):
    return [x for x in A if x in B], [x for x in set(list(A)+list(B))], [x for x in A if x not in B], [x for x in B if x not in A]

print(ex1([1,2,3,4,5],[3,4,5,6,7]))

# Ex 2
def ex2(s):
    dictionary = {}
    for c in s:
        if c in dictionary:
            dictionary[c] = dictionary[c] + 1
        else:
            dictionary[c] = 1
    return dictionary

print(ex2("Ana are mere."))

# Ex 3
def ex3(dict1, dict2):
    if set(dict1.keys()) != set(dict2.keys()):
        return False
    
    for key in dict1:
        value1 = dict1[key]
        value2 = dict2[key]
        
        if isinstance(value1, dict) and isinstance(value2, dict):
            if not ex3(value1, value2):
                return False
        elif isinstance(value1, list) and isinstance(value2, list):
            if len(value1) != len(value2) or any(a != b for a, b in zip(value1, value2)):
                return False
        elif value1 != value2:
            return False
    
    return True

dict1 = {
    "a": 1, "b": [2, 3], "c": { "d": 4, "e": [5, 6] }
}

dict2 = {
    "a": 1, "b": [2, 3], "c": { "d": 4, "e": [5, 7] }
}

print(ex3(dict1, dict2))

# Ex 4
def build_xml_element(tag, content, **kwargs):
    string = " ".join([a + "=\"" + b + "\"" for a, b in kwargs.items()])
    return "<{} {}> {} </{}>".format(tag, string, content, tag)


print(build_xml_element("a", "Hello there", href ="http://python.org", _class ="my-link", id= "someid"))

# Ex 5
def validate_dict(rules, dictionary):
    for t in rules:
        if t[0] in dictionary:
            v = dictionary.pop(t[0])
            if not (v.startswith(t[1]) and v.endswith(t[3]) and not v.startswith(t[2]) and not v.endswith(t[2])):
                return False

    return ( len(dictionary.keys()) == 0 )
    

print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                    {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))

# Ex 6
def ex6(li):
    a = 0
    b = 0
    for item in set(li):
        if li.count(item) == 1:
            a += 1
        else:
            b += 1

    return (a, b)

print(ex6([1, 2, 3, 4, 4, 4, 5, 6, 1, 79]))

# Ex 7
def ex7(*sets):
    if len(sets) < 2:
        return
    
    dictionary = {}

    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            a, b, c, d = ex1(sets[i], sets[j])
            dictionary["{} | {}".format(sets[i], sets[j])] = b
            dictionary["{} & {}".format(sets[i], sets[j])] = a
            dictionary["{} - {}".format(sets[i], sets[j])] = c
            dictionary["{} - {}".format(sets[j], sets[i])] = d
    
    return dictionary

print(ex7({1,2}, {2, 3}))

# Ex 8
def loop(mapping):
    visited = []
    key = 'start'
    while visited.count(key) == 0:
        visited.append(key)
        key = mapping[key]
    visited.remove('start')
    return visited


print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

# Ex 9
def ex9(*pargs, **kwargs):
    a = 0
    for item in kwargs.values():
        if pargs.count(item) > 0:
            a += 1
    return a
    
print(ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))