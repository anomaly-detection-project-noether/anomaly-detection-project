
def student_activity_plot(df):
    '''
    This function takes in a dataframe and returns a plot of the total count of student activity
    '''
    df[['start_date','end_date']] = df[['start_date','end_date']].apply(pd.to_datetime) #if conversion required
    df['total_days'] = (df['end_date'] - df['start_date']).dt.days

    df[['end_date','date']] = df[['end_date','date']].apply(pd.to_datetime) #if conversion required
    df['days_from_enddate'] = (df['date'] - df['end_date']).dt.days
    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)

    df = df.set_index('date')
    active_students_df= df.loc[df['days_from_enddate'] < 0]
    inactive_students_df= df.loc[df['days_from_enddate'] > 0]

    daily_hits = active_students_df['path'].resample('d').count()
    weekly_avg = daily_hits.ewm(span=7).mean()
    monthly_avg = daily_hits.ewm(span=30).mean()
    quarterly_avg = daily_hits.ewm(span=90).mean()

    daily_hitss = inactive_students_df['path'].resample('d').count()
    weekly_avgs = daily_hitss.ewm(span=7).mean()
    monthly_avgs = daily_hitss.ewm(span=30).mean()
    quarterly_avgs = daily_hitss.ewm(span=90).mean()

    daily_hitssss = df['path'].resample('d').count()
    weekly_avgsss = daily_hitssss.ewm(span=7).mean()
    monthly_avgsss = daily_hitssss.ewm(span=30).mean()
    quarterly_avgsss = daily_hitssss.ewm(span=90).mean()

    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True, figsize=(10, 8))
    fig.suptitle('Total Count of Student Activity', fontsize=12)
    fig.tight_layout()




    ax1.set_title("Active")
    #Plotting the resample of 'D' hits.
    ax1.plot(daily_hits, label='Original')
    #Plotting the resample of 'W' hits.
    ax1.plot(weekly_avg, label='Weekly')
    #Plotting the resample of 'M' hits.
    ax1.plot(monthly_avg, label='Monthly')
    #Plotting the resample of '3M' hits.
    ax1.plot(quarterly_avg, label='Quarterly')
    #Labels


    #Plotting the resample of 'D' hits.
    ax2.plot(daily_hitss, label='Original')
    #Plotting the resample of 'W' hits.
    ax2.plot(weekly_avgs, label='Weekly')
    #Plotting the resample of 'M' hits.
    ax2.plot(monthly_avgs, label='Monthly')
    #Plotting the resample of '3M' hits.
    ax2.plot(quarterly_avgs, label='Quarterly')
    #Labels
    ax2.set_title("Inactive")

    #Plotting the resample of 'D' hits.
    ax3.plot(daily_hitssss, label='Original')
    #Plotting the resample of 'W' hits.
    ax3.plot(weekly_avgsss, label='Weekly')
    #Plotting the resample of 'M' hits.
    ax3.plot(monthly_avgsss, label='Monthly')
    #Plotting the resample of '3M' hits.
    ax3.plot(quarterly_avgsss, label='Quarterly')
    #Labels
    ax3.set_title("Overall")


    #Show plot
    plt.show()
    
def top_15_plot(df):
    '''
    This function takes in a dataframe and returns a plot of the top 15 user ids by total count of paths
    '''
    ids= df.loc[df['name'].isnull()]

    new_ids_df =ids.groupby(by=['user_id']).count()

    new_ids_df['path'].sort_values(ascending=False).head(15).index

    sns.barplot(new_ids_df, 
                x=new_ids_df['path'].sort_values(ascending=False).head(15).index, 
                y=new_ids_df['path'].sort_values(ascending=False).head(15),
               palette="Spectral")
    plt.title("Top 15 User IDs By Total Count of Paths ")
    plt.ylabel("Path")
    plt.xlabel("User ID")
    plt.show()



def check_permissions(df, url):
    c = df[(df.start_date.str.startswith('2019')) & (df.program_id == 3) & (df[url].str.startswith('java'))]
    print(c)
    print()
    
def post_grad(df, program, url):
    b = df[(df.program_id == program) & (df.date > df.end_date) 
     & (df[url].str.startswith(('/', 'index', 'search'))== False)][url].value_counts().head()
    print(b)
    print()
    
def least_total(df, url, head, values):
    a = df[url].value_counts()[df[url].value_counts() > values].sort_values(ascending = True).head(head)
    print(a)
    print()

    
def least_cohort(df, url, head, values):
    coh = df.cohort_id.unique()    
    for i in coh:
        a = df[(df.cohort_id == i) & (df[url].str.startswith(('/', 'uploads', 'wp', '%', 'index'))== False)][url].groupby([df[url], df.name])
        b = a.value_counts()[a.value_counts() > values].sort_values(ascending = True).head(head)
        print(b)
        print()