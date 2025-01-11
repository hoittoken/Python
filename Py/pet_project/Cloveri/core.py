from sqlalchemy import text, insert, select, update
from database import sync_engine
from models import metadata_obj, interns_table, grades_table

class SyncCore:

    @staticmethod
    def create_tables():
        metadata_obj.drop_all(sync_engine)
        metadata_obj.create_all(sync_engine)

    @staticmethod
    def insert_interns():
        with sync_engine.connect() as conn:
            stmt = insert(grades_table).values(
                [
                    {'id':'f1',
                    'email':'work.aubakirov@gmail.com', 
                    'name':'Miguel Aubakirov',
                    'role':'Python-программист',
                    'internship':'Кабинет Кловери',
                    'start_date':'2025-01-15',
                    'end_date':'2025-04-28'
                     },
                    {'id':'f2',
                    'email':'work.aubakirov@gmail.com', 
                    'name':'Miguel Aubakirov',
                    'role':'Python-программист',
                    'internship':'MAIBO',
                    'start_date':'2025-01-15',
                    'end_date':'2025-04-28'
                     },
                     {'id':'f3',
                    'email':'sample@gmail.com', 
                    'name':'Nombre Apellido',
                    'role':'Python-программист',
                    'internship':'Кабинет Кловери',
                    'start_date':'2025-01-15',
                    'end_date':'2025-04-28'
                     },
                     {'id':'f4',
                    'email':'sample1@gmail.com', 
                    'name':'Jose Rodrigues',
                    'role':'QA-инженер',
                    'internship':'MAIBO',
                    'start_date':'2025-01-15',
                    'end_date':'2025-04-28'
                     },
                     {'id':'f5',
                    'email':'sample2@gmail.com', 
                    'name':'Soledad Lorna',
                    'role':'UX/UI-дизайнер',
                    'internship':'Платформа для ВУЗов',
                    'start_date':'2025-01-15',
                    'end_date':'2025-02-28'
                     }                                
                ]
            )
            conn.execute(stmt)
            conn.commit()

    @staticmethod
    def insert_grades():
        with sync_engine.connect() as conn:
            stmt = insert(grades_table).values(
                [
                    {
                    'id':'g1',
                    'intern_id':'f1',
                    'ai':4.4,
                    'programming':4.2,
                    'architecture':3.4,
                    'project_management':4.0,
                    'communication':5.4,
                    'personnel_management':3.4,
                    'information_management':5.4,
                    'infrastructure':4.7,
                    'data_management':3.4,
                    'math':5.8,
                    'data_analysis':4.0
                     },
                    {
                    'id':'g2',
                    'intern_id':'f2',
                    'ai':4.7,
                    'programming':4.8,
                    'architecture':4.4,
                    'project_management':4.3,
                    'communication':4.4,
                    'personnel_management':4.5,
                    'information_management':5.6,
                    'infrastructure':4.4,
                    'data_management':4.4,
                    'math':5.8,
                    'data_analysis':4.9
                     },
                     {
                    'id':'g3',
                    'intern_id':'f3',
                    'ai':4.3,
                    'programming':4.6,
                    'architecture':4.8,
                    'project_management':3.0,
                    'communication':3.4,
                    'personnel_management':4.4,
                    'information_management':3.6,
                    'infrastructure':4.0,
                    'data_management':3.4,
                    'math':3.3,
                    'data_analysis':4.0
                     },
                     {
                    'id':'g4',
                    'intern_id':'f4',
                    'ai':4.9,
                    'programming':4.9,
                    'architecture':5.8,
                    'project_management':6.0,
                    'communication':6.6,
                    'personnel_management':5.4,
                    'information_management':6.0,
                    'infrastructure':4.5,
                    'data_management':4.8,
                    'math':5.3,
                    'data_analysis':5.0
                     },
                     {
                    'id':'g4',
                    'intern_id':'f4',
                    'ai':4.9,
                    'programming':4.9,
                    'project_management':6.0,
                    'communication':6.6,
                    'personnel_management':5.4,
                    'information_management':6.0,
                    'infrastructure':4.5,
                    'visual':5.8,
                    'ux_ui':5.9,
                    'seo':4.4,
                    'typografy':4.5
                     }
                ]
            )
            conn.execute(stmt)
            conn.commit()

    @staticmethod
    def select_interns():
        with sync_engine.connect() as conn:
            query = select(interns_table) # SELECT * FROM interns
            result = conn.execute(query)
            interns = result.all()
            print(f"{interns=}")

    @staticmethod
    def update_interns(intern_id: str = 'f3', new_name: str = 'Ricardo Blanco'):
        with sync_engine.connect() as conn:
            #stmt = text("UPDATE cloveri.interns SET name=:new_name WHERE id=:intern_id")
            stmt = (
                update(interns_table)
                .values(name=new_name)
                #.where(interns_table.c.id == intern_id)
                .filter_by(id=intern_id)
            )
            #stmt = stmt.bindparams(new_name=new_name, intern_id=intern_id)
            conn.execute(stmt)
            conn.commit()

       