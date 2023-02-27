
import pandas as pd
df = pd.DataFrame()
print(df)

data = ["fd", "pt", 'wt']
df = pd.DataFrame(data, columns=['Pmt_Processor'])
print(df)

data = [['fd', 30], ['pt', 15], ['wt', 14]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
df

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







