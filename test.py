
import pandas as pd

s1 = [['FD', 302, 212121],
            ['FD', 596, 32434],
            ['FD', 530, 32342],
            ['FD', 612, 21233],
            ['PT', 5, 1233],
            ['PT', 14, 100],
            ['PT', 43, 1430],
            ['PT', 0O4, 213],
      ['WT', 5, 1233],
      ['WT', 39, 100],
      ['WT', 9, 1430],
      ['WT', 26, 213]
      ]
df = pd.DataFrame(s1,
                  columns=['PYMT_PRO', 'ERROR', 'CNT'])

print(df)



# Payment Processor	Error Node	Count
# Firstdata	302	21323
# Firstdata	596	1232
# Firstdata	530	2323
# Firstdata	612	21
# PaymentTech	05	21323
# PaymentTech	14	1232
# PaymentTech	43	2323
# PaymentTech	04	21
# wpwantif	005	21323
# wpwantif	039	1232
# wpwantif	009	2323
# wpwantif	‘026	21







