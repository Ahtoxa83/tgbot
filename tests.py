import psycopg2


f = open('password.txt', 'r')
password = f.read()
x = 5
connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                                   password=password, host='localhost')
cur = connect.cursor()
cur.execute(f"SELECT id,channel, leave_time FROM channel_entity WHERE bot_id = {x}")
all_channels = cur.fetchall()
for channel in all_channels:
    print(channel[0])
    print(channel[1])