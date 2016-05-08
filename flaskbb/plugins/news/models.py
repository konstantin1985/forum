from flaskbb.extensions import db

class NewsPost(db.Model):
    
    text = db.Column(db.String(3000), primary_key=True)
    
    def __repr__(self):
        return '<Text %r>' % (self.text)
    
