# # CODE TO DOWNLOAD THE CSV FILE FROM WEB:
# # =============================================================================
import pandas as pd
import numpy as np
import requests      
import datetime
import csv
from sortTwoJOIN import *

print("Enter path of .csv file: ")
target_csv_path = input() 
csvFileName = target_csv_path                                                                                                                                       # SAVE MASTER FILE
timeNow = datetime.datetime.now()
print(f"\n++++++++++ Please wait Downloading file ++++++++++ Current time:\n", str(timeNow) )

lastestTime = datetime.datetime.now()
timeTaken = lastestTime - timeNow
print(f"\n============> DOWNLOAD READY :)")
print("============> TIME TO DOWNLOAD:", str(timeTaken))

route1 = pd.read_csv(csvFileName)                                                                                                                                 # READ FILE
print(f'\r')
print( f' \r ============> LENGTH OF TABLE ',)                                                                                                                                              
print(f'LENGTH AND NUMBER OF PRICES:', len(route1))
print(f'\n ============> SHAPE OF IMPORTED TABLE')
print(f'SHAPE:', route1.shape)                                                                                                                                                                          
print(f'\r')
print(f' ============> SET PRICISION TO 2 DECIMAL PLACES')
pd.set_option("display.precision", 2)                                                                                                                                                                      
print(f' ============> SHOW INFO OF TABLE')
print(route1.info(), f'\n')
df = route1
print(f'============> CREATE route1 OBJECT')
print(f'============> REPLACE COLUMNS WITH SELECTION')
dataframe = pd.DataFrame(df, columns = ['SKU',                                                                                                            # WANTED COLUMNS
'Quantity', 
'Finished Size',
'Paper Type', 
'Print Type',
'Turnaround', 
'Lamination',
'VAT Rate', 
'Price £',  ])                                                                                                                                                                                        

print(f'Please enter your Maximum Quanity to Sort:')
maxQuantity = input()
frameRSLT = dataframe.loc[dataframe['Quantity'] <= int(maxQuantity)]
print(f'============> SELECTION IS LESS THAN OR EQUAL TO {maxQuantity}')
rowsSorted = frameRSLT.sort_values(by='Quantity', ascending = True)   
print(f'============> SORT ASCENDING FROM 0')
print(f'What will you call your sorted File?: ')
sortedName = input()
rowsSorted.to_csv(sortedName + f"Sorted_.csv")                                                                                                                # EXPORT FILE
print(f'\n============> EXPORT TO CSV FILE')
print(f'============> PRINT HEAD OF CLEANED TABLE:\n \n', rowsSorted.head(5), )

df = pd.read_csv(f"B:\\pythonPrintCompare\\sortJoin\\{sortedName}" + "Sorted_.csv")        

sortTwoJ(df)

