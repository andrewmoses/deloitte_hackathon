import sys
import pandas as pd

file_path = sys.argv[1]

jira_df = pd.read_csv(file_path)
unique_devs = jira_df['Assignee'].unique()
uniq_names = []
ticket_count = []
for each in unique_devs:
    tmp_df = jira_df.where((jira_df['Assignee']==each) & (jira_df['Status']=='Done'))
    fil_df = tmp_df[tmp_df['Assignee'].notnull()]
    ticket_count.append(fil_df['Assignee'].count())
    uniq_names.append(each)
for_df = {
    'email':uniq_names,
    'tickets_count':ticket_count
}
f_df = pd.DataFrame.from_dict(for_df)
f_df.to_csv("../outputs/jira.csv",index=False)
print("Succcess! check output at /outputs/jira.csv")

