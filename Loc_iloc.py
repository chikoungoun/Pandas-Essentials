""" Choisir plusieurs lignes et colonnes

* loc
* iloc
* (ix)
 """
import pandas as pd

url = 'Bruloir_datasets/ufo_reports.csv'
df = pd.read_csv(url)

print(df.head())
print(df.info())

""" loc """
#Format
# df.loc[ROWS,COLS]

print("\n * Une ligne, toutes les colonnes : ")
print(df.loc[0,:])#Renvoie un Series

print("\n * Les lignes 0,1,2 ; toutes les colonnes : ")
print(df.loc[[0,1,2] , : ])

print("\n * Les lignes 30,69,101 ; toutes les colonnes : ")
print(df.loc[[30,69,101] , : ])

""" Ne pas indiques les colonnes est considéré comme les sélectionner toutes"""

print("\n * Toutes Les lignes  ; la colonne 'city' : ")
print(df.loc[:,'City'])#Renvoie une Series


print("\n * Toutes Les lignes  ; la colonne 'city' et 'State': ")
print(df.loc[:,['City','State']])

print("\n * Les lignes 0 a 2  ; la colonne 'city' et 'State' : ")
print(df.loc[0:2,'City'])

print("\n * Filtrer uniquement la ville 'Oakland' : ")
print(df[df.City == 'Oakland'])

print("\n * Filtrer uniquement la ville 'Oakland' : (version avec loc) ")
print(df.loc[df['City'] == 'Oakland' , : ])

print("\n * Filtrer uniquement la ville 'Oakland' ; afficher uniquement 'State' ")
print(df.loc[df['City'] == 'Oakland' , 'State' ])

#Achtung
# non-explicit : df[['City','State']]
# explicit     : df.loc[ : , ['City','State']]

""" iloc : fonctionne uniquement avec les index"""
print("\n \n \n *********** iloc ************* ")
print(df.iloc[:,0:4])

""" iloc forme des intervalles exclusifs """
print("\n * lignes 0 à 2 ; toutes les colonnes ")
print(df.iloc[0:3 , : ])

print("\n * lignes 1,3,5 ; les colonnes 1, 3 ")
print(df.iloc[[1,3,5] , [1,3]])
