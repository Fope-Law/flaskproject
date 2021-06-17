from app import db, Products, Purchases, Customers

db.drop_all()
db.create_all()

person1 = Customers(name='Femi')
person2 = Customers(name='Tiwa')

db.session.add(person1)
db.session.add(person2)
db.session.commit()

item1 = Products(name='shampoo')
item2 = Products(name='conditioner')
db.session.add(item1)
db.session.add(item2)
db.session.commit()

purchase1 = Purchases(customer = person1, product = item1)
purchase2 = Purchases(customer = person2, product = item1)
purchase3 = Purchases(customer = person2, product = item2)
db.session.add(purchase1)
db.session.add(purchase2)
db.session.add(purchase3)
db.session.commit()
