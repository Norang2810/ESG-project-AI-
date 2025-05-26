#%%
dic6 = {
    'A001' : {'name':'Lee' ,'age' :10,'job':'농부'},
    'A002' : {'name':'Park','age':30,'job':'의적'}       
}

print(dic6)
# %%
del dic6['A001']['age']
del dic6['A002']['age']

dic6
# %%

for key,value in dic6.items():
    for key2,value2 in value.items():
        print('{}\t'.format(value2),end="")   
        print()