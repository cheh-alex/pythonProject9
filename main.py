from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase('mydb.sqlite')
db.connect()


class User(Model):
    name = CharField(max_length=50)
    age = IntegerField()
    city = CharField(max_length=50)

    class Meta:
        database = db
        db_table = 'users'


User.create_table()

# CRUD () Create Read Update Delete

#Create
u1 = User(name="Viktor", age=21, city="Kiev")
print(u1)
u1.save()  # write into database
print(u1)


#Read

# Read all rows

users = User.select()
for u in users:
    print(u.name)

#Read by ID
user1 = User.get_by_id(1)
print(user1.name)

#Read by query
user_maksim = User.get(User.name == "Alex")
print(user_maksim.age)


# Update

# # find row to change
user = User.get(User.name == 'Maksim')
print(user.name, user.age)

# change the object of model
user.name = 'Alex'

# save changed object
user.save()


# Delete
# find element to delete from db
user = User.get(User.name == 'Alex')
print(user)
#
# delete element
user.delete_instance()