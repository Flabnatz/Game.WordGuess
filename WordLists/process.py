import pandas as pd

def mk_csv(file, XL_DIR, CSV_DIR):
   fname = XL_DIR+file+'.xlsx'

   wdata = pd.read_excel(fname, skiprows=1)
   rows = wdata.values

   words = []
   for row in rows:
      words.extend(row)

   cleanwords = [x for x in words if str(x) != 'nan']
   df = pd.DataFrame(cleanwords, columns=["word"])
   df.to_csv(CSV_DIR+file+'.csv')

   print('Created '+file+'.csv file.')