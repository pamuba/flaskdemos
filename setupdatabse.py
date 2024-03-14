from basic_models import db, Puppy

# CREATES ALL THE TABLES FROM MODELS --> DB TABLES
db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

# None
print(sam.id)
print(frank.id)

db.session.add_all([sam,frank])

# db.session.add(sam)
# db.session.add(frank)

db.session.commit()

print(sam.id)
print(frank.id)

