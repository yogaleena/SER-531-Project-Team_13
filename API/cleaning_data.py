import pandas as pd

data_field = pd.read_csv('TweetClean.csv')
data_field2 = data_field.dropna(axis=0, subset=["Date", "Tweet_Text", "Source", "User_ID", "Lat", "Lng"])
data_field3 = data_field2[~data_field2['Tweet_Text'].str.contains(r'[^\x00-\x7F]+')]
data_field4 = data_field3[~data_field3['Source'].str.contains(r'[^\x00-\x7F]+')]
new_data_field = data_field4.to_csv('NewTweetClean.csv', index=False)

data_field = pd.read_csv('UserClean.csv')
data_field2 = data_field.dropna(axis=0, subset=["ID", "Name", "Screen_Name", "User_Location"])
data_field3 = data_field2[~data_field2['Name'].str.contains(r'[^\x00-\x7F]+')]
data_field4 = data_field3[~data_field3['User_Location'].str.contains(r'[^\x00-\x7F]+')]
new_data_field = data_field4.to_csv('NewUserClean.csv', index=False)

data_field = pd.read_csv('eventclean.csv')
keep_columns= ["event_id", "start_time", "city", "state", "country", "lat", "lng"]
n_df = data_field[keep_columns]
n_df = n_df.dropna(axis=0, subset=['event_id', 'start_time', 'city', 'state', 'country'])
n_df.to_csv("Newevents_clean.csv", index=False)

data_field2 = pd.read_csv('users.csv')
n_df2 = data_field2.dropna(axis=0, subset=['user_id', 'locale', 'birthyear', 'gender', 'joinedAt', 'location', 'timezone'])
n_df2.to_csv("Usersid_clean.csv", index=False)
