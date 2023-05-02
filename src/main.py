import pandas as pd 


dictionary = {"columna_1": [1,2,3,4],'columna_2':[5,6,7,8]}

dataframe = pd.DataFrame(dictionary)



def sumar (a:int,b:int):
    return a + b 

def restar (a:int,b:int):
    return a - b 

if '__name__' == "__main__":
    
    print (f"la resta de 2 - 1 es : {restar(2,1)}")

