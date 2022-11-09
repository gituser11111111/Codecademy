import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv',
                        parse_dates=[1])

# Part 1: print to inspect each DataFrame
print(visits.head(10))
print(checkouts.head(10))

# Part 2: merge visits and checkouts
v_to_c = pd.merge(visits, checkouts)

# Part 3: define the column time to be the different between checkout time and visit time
v_to_c['time'] = v_to_c.checkout_time - v_to_c.visit_time

print(v_to_c.time.mean())
