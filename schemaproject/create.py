from app import db, Users

db.drop_all()
db.create_all()

testuser = Users(first_name='Harry', last_name='Bo')
db.session.add(testuser)
db.session.commit()




































