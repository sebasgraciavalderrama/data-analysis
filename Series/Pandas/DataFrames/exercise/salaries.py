import pandas as pd

df_csv = pd.read_csv('Salaries.csv')
print(df_csv)
head_df_csv = df_csv.head()
print(df_csv.info())
avg_base_pay = df_csv['BasePay'].mean()
print(avg_base_pay)
high_amount_overtime = df_csv['OvertimePay'].max()
print(high_amount_overtime)
joseph_driscoll = df_csv.loc[df_csv['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
print(joseph_driscoll)
joseph_driscoll_income = df_csv.loc[df_csv['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
print(joseph_driscoll_income)
highest_paid_person = df_csv[df_csv['TotalPayBenefits'] == df_csv['TotalPayBenefits'].max()]
print(highest_paid_person)
lowest_paid_person = df_csv[df_csv['TotalPayBenefits'] == df_csv['TotalPayBenefits'].min()]
print(lowest_paid_person)

#average_basepay_by_year = df_csv.loc['2011', '2012', '2013', '2014']
#average_basepay_by_year = df_csv[(df_csv['Year'] == '2011') & (df_csv['Year'] == '2012') & (df_csv['Year'] == '2013') & (df_csv['Year'] == '2014')] # Conditional selectio
average_basepay_by_year = df_csv.groupby('Year').mean()['BasePay']
print(average_basepay_by_year)

unique_job_titles = df_csv['JobTitle'].nunique()
print(unique_job_titles)

five_most_common_jobs = df_csv['JobTitle'].value_counts().head(5)
print(five_most_common_jobs)

job_titles_represented_by_one = sum(df_csv[df_csv['Year'] == 2013]['JobTitle'].value_counts() == 1)

print('\n')
# How many people have the word Chief in their job title? (This is pretty tricky)
def chief_string(title):
    if 'chief' in title.lower():
        return True
    return False

people_with_chief_jobtitle = sum(df_csv['JobTitle'].apply(lambda x: chief_string(x)))
print(people_with_chief_jobtitle)