
import os
import pandas as pd





def lesson_most_accessed(df):
    
    '''this function takes in a dataframe, creates columns to
    identify each cohort by Boolean value, then returns the most-
    accessed lesson for each Codeup programme'''
    
    # find all the PHP full stack cohorts
    df['php_cohort'] = np.where(df['program_id'] == 1, 1, 0)

    # find all the full stack / java cohorts
    df['fs_java_cohort'] = np.where(df['program_id'] == 2, 1, 0)

    # find all the data science cohorts
    df['ds_cohort'] = np.where(df['program_id'] == 3, 1, 0)

    # find all the front end cohorts
    df['front_end_cohort'] = np.where(df['program_id'] == 4, 1, 0)

    # most-accessed PHP lesson is javascript-i (if not counting index.html, which was accessed more)
    php = df[df['php_cohort'] == 1]['path'].value_counts().iloc[2:3]

    # most-accessed full-stack _ java lesson is javascript-i
    fsj = df[df['fs_java_cohort'] == 1]['path'].value_counts().iloc[1:2]

    # most-accessed DS lesson is the classification overview
    ds = df[df['ds_cohort'] == 1]['path'].value_counts().iloc[2:3]

    # most-accessed front-end lesson is content/html-css 
    fe = df[df['front_end_cohort'] == 1]['path'].value_counts().head(1)
    
    print(f'The most accessed PHP cohort lesson page is {php}.') 
    print(f'The most accessed full-stack java cohort lesson page is {fsj}.')
    print(f'The most accessed data science cohort lesson page is {ds}.')
    print(f'The most accessed front-end cohort lesson page is {fe}.')
    
    
    
    
# loop through all 'name' and get most-accessed page

def url_most_accessed(df):
    
    '''
    this function takes in a daframe, isolates the cohort names,
    loops through each cohort name, ignores urls starting with 
    punctuation characters, indices, search pages, etc, and
    returns the 2 most-accessed webpages for each cohort.
    '''
    
    # get unique cohort names
    cohort_names = df['name'].unique()
    
    # loop through each cohort name
    for i in cohort_names:

        # for each cohort name, ignore any url path that starts with punctuation, etc
        # group by programme id, url path and return the 2 most-accessed webpage urls
        coh = df[(df['name'] == i) & (df['url_path'].str.startswith(('/', 'index','search', '.', 
                                                    '%', ',',"'",'00_',
               'Index')) == False)].groupby('url_path')['program_id'].count().sort_values(ascending = False).head(2)


        # print cohort name, 2 top webpages hit
        print(i, coh)
        
        # prints a space between cohorts
        print()

    
        