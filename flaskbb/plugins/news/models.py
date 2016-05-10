from flaskbb.extensions import db

class MyPost(db.Model):
    name = db.Column(db.String(200), primary_key=True)
    text = db.Column(db.String(3000))
    
    def __repr__(self):
        return '<Text %r>' % (self.text)
    
