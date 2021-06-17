from app import db, Countries, Cities
db.create_all() # Creates all table classes defined

UK = Countries(name = 'United Kingdom') #Add example to countries table
db.session.add(UK)
db.session.commit()

# Here we reference the country that london belongs to using 'country', this is what we named the backref variable in db.relationship()
ldn = Cities(name='London', country = UK)

db.session.add(ldn)
db.session.commit() 