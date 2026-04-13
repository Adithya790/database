from pymongo import mongoclient
client = mongoclient ("mongodb+srv://adiadithyaajayan_db_user:wTsfJOqgVtYlP4u0@cluster0.oatty2n.mongodb.net/?appName=Cluster0")
database = client['practise']
collection = database ['tados']
task = {"title":'read',"is_completed":False}
# Add single data
result1= collection.insert_one(task)
# Add multiple data
result = collection.insert_many([
    {"title": "Write", "is_completed": False},
    {"title": "Paint", "is_completed": False}
])
# Remove single data
collection.delete_one({"title": "Write", "is_completed": False})
# Retrieve multiple data
tasks = collection.find({"is_completed": False}, {"_id": 0, "title": 1})
# Print tasks
for task in tasks:
    print(task, "in for loop")
# Update single data
collection.update_one(
    {"title": "Read"},
    {"$set": {"is_completed": False}}
    )
# Retrieve single data
data = collection.find_one({"is_completed": True})
print(data)