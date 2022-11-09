import codecademylib3
import pandas as pd

df = pd.read_csv('inventory.csv')

df.head(10)

staten_island = df.head(10)

product_request = staten_island['product_description']

seed_request = df[(df.location == 'Brooklyn') & (df.product_type == 'seeds')]

df['in_stock'] = df.apply(lambda row: True if row.quantity > 0 else False, axis = 1 )

df['total_value'] = df.apply(lambda row: row.price * row.quantity, axis = 1)

combine_lambda = lambda row: \
  '{} : {}'.format(row.product_type, row.product_description)

df['full_description'] = df.apply(combine_lambda, axis = 1)

print(df.head(15))
