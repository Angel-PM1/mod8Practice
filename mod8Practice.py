def frequency(a_str: str)-> dict:
    assert type(a_str) == str

    d_count={}


    for char in a_str:
        if char not in d_count:
            d_count[char]=1
        else:
            d_count[char]=d_count[char]+1

    return d_count

def get_mixed(d1:dict,d2:dict) -> dict:
    assert type(d1) == dict and type(d2) == dict

    new_d={}

    for key,value in d1.items():
        if value in d2:
            new_d[key] = d2[value]

    return new_d

def reverse_lookup(d:dict,element):
    for key,value in d.items():
        if value == element:
            return key
        
def magic_keys(d:dict,num:int)-> list:
    assert type(d) == dict and type(num) == int
    assert num >= 0


    key_lst = []

    for key,value in d.items():
        if type(value) == str and len(value.split()) == num:
            key_lst.append(key)

    return key_lst

def classify_numbers(lst:list)-> dict:
    assert type(lst) == list

    d= {"even":[],"odd":[]}
    for num in lst:
     
        if num % 2 ==0:
            d["even"].append(lst[num])
        else:
            d["odd"].append(lst[num])
    
    return d

def by_course(d:dict) ->dict:
    assert type(d) == dict

    new_d = {}

    for student,courses in d.items():
        for course in courses:
            if course not in new_d:
                new_d[course] = []
            new_d[course].append(student)
    
    return new_d






















def main():
    #-YOUR ASSERTIONS TO TEST FOR YOUR FUNCTIONS STARTS HERE (TODO)
    pass

if __name__ == "__main__":
    main()
