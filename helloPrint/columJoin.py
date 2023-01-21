# from functools import reduce
# import pandas as pd
# import numpy as np
# import requests      
# import datetime
# import csv
# # from sortTwoJOIN import *

# print("Enter path of .csv file: ")
# target_csv_path = input() 
# csvFileName = target_csv_path                                                                                                                                       # SAVE MASTER FILE
# timeNow = datetime.datetime.now()
# print(f"\n++++++++++ Please wait Downloading file ++++++++++ Current time:\n", str(timeNow) )
# lastestTime = datetime.datetime.now()
# timeTaken = lastestTime - timeNow
# print(f"\n============> DOWNLOAD READY :)")
# # print("============> TIME TO DOWNLOAD:", str(timeTaken))
# # route1 = pd.read_csv(csvFileName)                                                                                                                                 # READ FILE
# print(f'\r')
# print( f' \r ============> LENGTH OF TABLE ',)                                                                                                                                              
# print(f'LENGTH AND NUMBER OF PRICES:', len(route1))
# print(f'\n ============> SHAPE OF IMPORTED TABLE')
# print(f'SHAPE:', route1.shape)                                                                                                                                                                          
# print(f'\r')
# print(f' ============> SET PRICISION TO 2 DECIMAL PLACES')
# pd.set_option("display.precision", 2)                                                                                                                                                                      
# print(f' ============> SHOW INFO OF TABLE')
# print(route1.info(), f'\n')
# df = route1
# tpTable1 = pd.read_csv("B:/pythonPrintCompare/sortJoin/TPFlyersExpress~SortTwo_.csv")                                                       # takes-in flyer standard | saver | express files
# tpTable2 = pd.read_csv("B:/pythonPrintCompare/sortJoin/TPFlyersStandard~SortTwo_.csv")
# tpTable3 = pd.read_csv("B:/pythonPrintCompare/sortJoin/TPFlyersSaver~SortTwo_.csv")

def reName(df):

    df.reset_index(drop=True, inplace=True)
    #     "Express Sku": "SKU", "PriceExpress":"Price", "Production Days Express":"Production",
    # df1 = pd.DataFrame(tpTable11)
    # df1.drop(['Turnaround'], axis=1, inplace=True)
    df.rename(columns= {"sku": "SKU","quantity":"Quantity","@material":"Paper Type","@printing":"Sides Printed","servicelevel":"Service Level","@size":"Size", "price":"Price", "productiondays":"Turnaround"}, inplace=True)

 #   tpAppended = pd.concat([df1, df2, df3], axis=0, ignore_index=1)
    dropCol = df.drop('Unnamed: 0', axis=1)
    dropCol.reset_index(drop=True)

    print(dropCol.head(3))

    dropCol.to_csv("HPjoinedTable.csv")

    print(f'What will you call your Master File?: ')
    sortedName = input()

    dropCol.to_csv(sortedName + f"~SortMaster_.csv")                                                                                  # EXPORT FILE
    print(f'\n============> EXPORTED TO MASTER  CSV FILE')
    print(f'============> PRINT HEAD OF CLEANED TABLE:\n \n', dropCol.head(5), )

    return
# tpTable22 = tpTable2
# # # #     "Standard Sku": "SKU", "PriceStandard":"Price", "Production Days Standard":"Production",
# df2 = pd.DataFrame(tpTable22)
# # df2.drop(['Turnaround'], axis=1, inplace=True)
# df2.rename(columns= {"Standard Sku": "SKU", "PriceStandard":"Price", "Production Days Standard":"Turnaround"}, inplace=True)
# tpTable33 = tpTable3
# # # #     "Saver Sku": "SKU", "PriceSaver":"Price", "Production Days Saver":"Production",})
# df3 = pd.DataFrame(tpTable33)
# df3.drop(['Turnaround'], axis=1, inplace=True)
# df3.rename(columns= {"Saver Sku": "SKU", "PriceSaver":"Price", "Production Days Saver":"Turnaround"}, inplace=True)
# #print(f'============> PRINT HEAD OF CLEANED TABLE:\n \n', tpTable1.head(3), )
# # print(f'============> PRINT HEAD OF CLEANED TABLE:\n \n', tpTable2.head(3), )
# # print(f'============> PRINT HEAD OF CLEANED TABLE:\n \n', tpTable3.head(3), )
# #route1 = [tpTable11, tpTable22, tpTable33]
# # #route1 = df[tpTable11, tpTable22, tpTable33]
# # #print(route1.columns)
# # route1 = reduce(lambda  left,right: pd.merge(left,right,on=['SKU'],how='outer'), route1).fillna('none')
# # t = [tpTable11, tpTable22, tpTable33]
# # for n in t:
# #     reName = pd.DataFrame(t)
# #     reName.rename(columns = {
# #print(df.head(3))


#joinRead = pd.read_csv("B:\pythonPrintCompare\sortJoin\joinedTable.csv")
# print(f'============> PRINT HEAD OF CLEANED TABLE:\n \n', tpTable1.head(5), )












# import numpy as np
# import pandas as pd

# def createList(r1, r2):
#     return np.arange(r1, r2+1)                                                                      

# dfSAMPLE = createList(0,5)                                                                                      # start | end values for columns
# dfFILE = pd.DataFrame([dfSAMPLE])



# dfFILE.apply(lambda x: ','.join(x.astype(str)))                                                            #3.47 s ± 24.5 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
# dfFILE.astype(str).agg(', '.join, axis=1)                                                                      #34.8 ms ± 407 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

# print(dfFILE)