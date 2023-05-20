from App.models import Rubric
from App.database import db

def create_rubric(supervisorId, novelty, feasibility, notes, impact, sustainability):
    rubric = Rubric(supervisorId, novelty, feasibility, notes, impact, sustainability)
    db.session.add(rubric)
    db.session.commit()
    return rubric

def delete_rubric(rubricId):
    rubric = Rubric.query.get(rubricId)
    if rubric :
        db.sesion.delete(rubric)
        res = db.session.commit()
        return res
    return None

def get_user_rubric(supervisorId, rubricId):
    rubric = Rubric.query.filter_by(supervisorId=supervisorId, rubricId=rubricId).all()
    return rubric
    

def get_user_rubrics(supervisorId):
    return Rubric.query.filter_by(supervisorId=supervisorId).all()

def get_all_rubrics():
    return Rubric.query.all()

def get_rubric(rubricId):
    return Rubric.query.get(rubridId)