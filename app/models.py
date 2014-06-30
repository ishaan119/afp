__author__ = 'ishaansutaria'
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    #last_feedback = db.Column.()
    last_seen = db.Column(db.DateTime)
    work_title = db.Column(db.String(140))
    applicants = db.relationship('Applicant', backref = 'interviewer', lazy = 'dynamic')
    '''
    reviewer = db.relationship('User',
                               secondary = reviewer,
                               primaryjoin = (reviewer.c.reviewer_id),
                               secondaryjoin = (reviewer.c.admin_id),
                               backref = db.backref('reviewer', lazy = 'dynamic'), 
                               lazy = 'dynamic')
    '''

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)
    
    @staticmethod
    def make_unique_nickname(nickname):
         if User.query.filter_by(nickname = nickname).first() == None:
                return nickname
         version = 2
         while True:
                new_nickname = nickname + str(version)
                if User.query.filter_by(nickname = new_nickname).first() == None:
                    break
                version += 1
         return new_nickname

class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    applicant_name = db.Column(db.String(200))
    position = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    appraisal_of_self = db.Column(db.Integer)
    interest_in_field = db.Column(db.Integer)
    carrer_goals = db.Column(db.Integer)
    skills = db.Column(db.Integer)
    accomplishment = db.Column(db.Integer)
    relevant_experience = db.Column(db.Integer)
    potential = db.Column(db.Integer)
    creativity = db.Column(db.Integer)
    logic = db.Column(db.Integer)
    comments = db.Column(db.String(500))
    recommendation = db.Column(db.Integer)

    def __repr__(self):
        return  '<Applicant %r>'%self.applicant_name
 
'''   
reviewer = db.Table('reviewer',
                     db.Column('reviewer_id',db.Integer,db.ForeignKey('user.id')),
                     db.Column('admin_id',db.Integer,db.ForeignKey('user.id'))
                     )
'''




