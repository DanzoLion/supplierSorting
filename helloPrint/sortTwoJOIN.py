# for sorting the table by Product Tile & Keeping only those products | Removing Unwanted Products from a list
import pandas as pd
#from sortOne_MAIN import *
# Making data frame from the csv file

#route2

def sortTwoJ(df):

    #df = pd.read_csv(df)
    sortedTable = pd.DataFrame(df, columns = [                                                                                     # these columns must match columns from first sort
'sku',                                                                                                            
'quantity', 
'servicelevel',
'productiondays',
'price', 
'@material',
'@printing', 
'@size',
])                       

    print("Columns Are selected", ) 

    options = [                                                                                                                                         # this is the option picker, these are the options we want from columns below
        '170gsilk', 


    ]
    

    sortedRows = sortedTable.loc[                                                                                                           # these are the columns we look into
        (sortedTable['@material'].isin(options))  #&
       # (sortedTable['Lamination'].isin(options)) 

    #    (sortedTable['VAT Rate'].isin(options)) &
    #    (sortedTable['Turnaround'].isin(options)]
    ]
    print(f'\r')
    print( f' \r ============> LENGTH OF TABLE ',)                                                                                                                                              
    print(f'LENGTH AND NUMBER OF PRICES:', len(sortedRows))
    print(f'\n ============> SHAPE OF IMPORTED TABLE')
    print(f'SHAPE:', sortedRows.shape)                                                                                                                                                                          
    print(f'\r')
    print(f' ============> SET PRICISION TO 2 DECIMAL PLACES')
    pd.set_option("display.precision", 2)                                                                                                                                                                      
    print(f' ============> SHOW INFO OF TABLE')
    print(sortedRows.info(), f'\n')

    print(f'What will you call your sorted File?: ')
    sortedName = input()

    sortedRows.to_csv(sortedName + f"~SortTwo_.csv")                                                                                  # EXPORT FILE
    print(f'\n============> EXPORT TO CSV FILE')
    print(f'============> PRINT HEAD OF CLEANED TABLE:\n \n', sortedRows.head(5), )

    return

#sortTwoJ(df)



