# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:35:12 2020

@author: Samantha
"""

def test():
    D1={1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'e'}
    num_parts = 3
    count = 0
    at_dict = 0
    avg_len = len(D1) / float(num_parts)
    round_avg = int(avg_len)
    left_over = len(D1) % num_parts
    print("left over")
    print(left_over)
    left_in = len(D1) // num_parts
    print("left in")
    print(left_in)
    #list_dicts = [None] * num_parts
    list_dicts = [{}] * num_parts
    new_dict = {}
    #num_thru = 0
    #for k in D1.keys():
   #print (k, D1[k])
   
    #for k, v in D1.items():
        #print(k, v)
    print(list_dicts)
    print("meep")

    for k in D1.keys():
    #[x for x in D1]:
        
        #if (count == int(avg_len)):
        if (count == round_avg):
            print("entered first if")
            #list_dicts.append(new_dict)
            count = 0
            new_dict = {}
            at_dict += 1
            print("At dict")
            print(str(at_dict))
            #num_thru += 1
            #print("Num thru")
            #print(num_thru)
            if (at_dict == num_parts):
                at_dict = 0
                #num_thru = 0
                print("at dict")
                print(at_dict)
            
            
        if count < round_avg:
            print("entered second if")
            #print("Num thru")
            #print(num_thru)
            new_dict[k] = D1[k]
            print("New dict")
            print(new_dict)
            count += 1
            print("count")
            print(count)
            #if (count == round_avg):
                #list_dicts.append(new_dict)
                #list_dicts[at_dict] = new_dict
                #list_dicts[at_dict].update(new_dict)
            current_dict = list_dicts[at_dict]
            list_dicts[at_dict] = {**current_dict, **new_dict}
            #break
            #break
            #new_dict[x] = D1[x]
            
       # list_dicts[at_dict] = new_dict
       # list_dicts.append(new_dict)
        #print(list_dicts)
        #new_dict = {}    
        #count += 1
        #while count < (2 * avg_len):
        #while count < 1:
            #print (k, v)
            #count += 1
    print(list_dicts)
    return list_dicts
    
def test2():
    D2={1:'a', 2:'b', 3:'c'}
    for k, v in D2.items():
        print(k, v)

#test2()
#print("meep")
#test()
#print(test())

