from pymongo import MongoClient

client= MongoClient('localhost',27017)

db=client['mydb']

print("Database created ---")
print(client.list_database_names())
