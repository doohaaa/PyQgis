_WHERE_TOT_FIELD = 5
_WHERE_GRID_ID_FIELD = 6

## feature dict 가 뭔지 확인 
layer= iface.activeLayer()


# Create a dictionary of all feature
feature_dict = {f.id(): f for f in layer.getFeatures()}

for i in range(0,len(feature_dict)):
    ####print("i : %d" %i)
    for j in range(i+1,len(feature_dict)):
        
        a=feature_dict.get(i)
        b=feature_dict.get(j)
        c=feature_dict[i]
        
        
        ####print(j)
        
        if(a.attributes()[_WHERE_TOT_FIELD]>1500):
            print(a.attributes()[_WHERE_TOT_FIELD])
        ###print(b.attributes()[_WHERE_GRID_ID_FIELD])
    print("")
    
####print(c)
####print(c.attributes()[_WHERE_GRID_ID_FIELD])
####print(a.attributes()[_WHERE_GRID_ID_FIELD])


print("process complete")