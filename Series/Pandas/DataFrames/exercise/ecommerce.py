import pandas as pd

ecom = pd.read_csv('Ecommerce Purchases')
print(ecom)
head_ecom = ecom.head()
print(head_ecom)
print(ecom.info())

# Average purchase price
average_purchase_price = ecom['Purchase Price'].mean()
print(average_purchase_price)

# Highest and lowest pruchase prices
max_purchase_price = ecom['Purchase Price'].max()
min_purchase_price = ecom['Purchase Price'].min()
print(max_purchase_price)
print(min_purchase_price)

# How many people have English 'en' as their Language of choice
count_en_people = sum(ecom[ecom['Language'] == 'en'].value_counts() == 1)
# ecom[ecom['Language']=='en'].count()
print(count_en_people)


# How many people have the job title of 'Laywer'
count_lawyers = sum(ecom[ecom['Job'] == 'Lawyer'].value_counts() == 1)
#ecom[ecom['Job'] == 'Lawyer'].info()
print(count_lawyers)

# How many people made the purchase during the AM and how many during PM
am_pm_purchases = ecom['AM or PM'].value_counts()
print(am_pm_purchases)


# What are the 5 most common Job Titles
five_most_common_jobs = ecom['Job'].value_counts().head(5)
print(five_most_common_jobs)

purchase_price = ecom[ecom['Lot'] == '90 WT']['Purchase Price']
print(purchase_price)

credit_card = ecom[ecom['Credit Card'] == 4926535242672853]['Email']
print(credit_card)

american_express_and_greater_95 = sum(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 94)].value_counts() == 1)
print(american_express_and_greater_95)

# Hard: How many people have a credit card that expires in 2025?

def ends_with_25(title):
    if title.endswith('25'):
        return True
    return False

expiration_date_with_25 = sum(ecom['CC Exp Date'].apply(lambda x: ends_with_25(x)))
print(expiration_date_with_25)


print(ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))