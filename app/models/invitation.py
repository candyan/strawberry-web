import hashlib
import random
from utils.store import db


class InvitationCode(db.Model):
    __tablename__ = "invitation_code"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(16), unique=True)
    used = db.Column(db.Boolean, default=False)

    def __init__(self, code):
        self.code = code
        self.used = False

    def __repr__(self):
        if self.used:
            return '<InvitationCode %r is used>' % self.code
        else:
            return '<InvitationCode %r is not used' % self.code

    def use(self):
        self.used = True
        if self.id:
            db.session.commit()

    @classmethod
    def get_by_code(cls, code):
        return InvitationCode.query.filter_by(code=code).first()

    @classmethod
    def get_unused_codes(cls, code):
        return InvitationCode.query.filter_by(used=False).all()

    @classmethod
    def add_invitation_codes(cls, amount=1):
        if amount == 0:
            return True

        for index in range(amount):
            random_code = hashlib.sha1("%d" % random.randint(0, 99999999))
            invitation_code = random_code.hexdigest()[:16].upper()
            db.session.add(InvitationCode(code=invitation_code))
        db.session.commit()
        return True

    @classmethod
    def unused_count(cls):
        return InvitationCode.query.filter_by(used=False).count()
