import datetime
from sqlalchemy import Boolean, Table, Column, Float, String, Date, MetaData, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base, str_100, str_320

# for using in core mod

class InternsOrm(Base):
    __tablename__ = "interns"
    __table_args__ = {"schema": "cloveri"}
    id: Mapped[str] = mapped_column(primary_key=True)
    email: Mapped[str_320]
    name: Mapped[str_100]
    role: Mapped[str_100]
    internship: Mapped[str_100]
    start_date: Mapped[datetime.datetime]
    end_date: Mapped[datetime.datetime]
    notes: Mapped[str | None]

class GradesOrm(Base):
    __tablename__ = "grades"
    __table_args__ = {"schema": "cloveri"}
    intern_id: Mapped[str] = mapped_column(ForeignKey(InternsOrm.id, ondelete="CASCADE"))
    id: Mapped[str] = mapped_column(primary_key=True)
    ai: Mapped[float | None]
    programming: Mapped[float | None]
    architecture: Mapped[float | None]
    project_management: Mapped[float | None]
    communication: Mapped[float | None]
    personnel_management: Mapped[float | None]
    information_management: Mapped[float | None]
    infrastructure: Mapped[float | None]
    data_management: Mapped[float | None]
    math: Mapped[float | None]
    data_analysis: Mapped[float | None]
    visual: Mapped[float | None]
    ux_ui: Mapped[float | None]
    seo: Mapped[float | None]
    typografy: Mapped[float | None]
    skill18: Mapped[float | None]
    skill19: Mapped[float | None]
    skill20: Mapped[float | None]

class ToolsOrm(Base):
    __tablename__ = "tools"
    __table_args__ = {"schema": "cloveri"}
    #skills_role: Mapped[str_100] = mapped_column(ForeignKey(InternsOrm.role, ondelete="CASCADE"))
    #skills_internship: Mapped[str_100] = mapped_column(ForeignKey(InternsOrm.internship, ondelete="CASCADE"))
    id: Mapped[str] = mapped_column(primary_key=True)
    role: Mapped[str_100]
    internship: Mapped[str_100]
    pycaret: Mapped[bool | None]
    random_Forest: Mapped[bool | None]
    anomaly_Detеction: Mapped[bool | None]
    gradient_Boosting: Mapped[bool | None]
    cluster_analysis: Mapped[bool | None]
    k_fold: Mapped[bool | None]
    optuna: Mapped[bool | None]
    shap: Mapped[bool | None]
    tsfresh: Mapped[bool | None]
    sklearn_feature_selection: Mapped[bool | None]
    imblearn: Mapped[bool | None]
    Streamlit: Mapped[bool | None]
    Selenium: Mapped[bool | None]
    Allure: Mapped[bool | None]
    Nose: Mapped[bool | None]
    SimpleTest: Mapped[bool | None]
    Docker: Mapped[bool | None]
    Jira: Mapped[bool | None]
    Adobe_XD: Mapped[bool | None]
    Figma : Mapped[bool | None]
    Mockplus: Mapped[bool | None]
    Yandex_metrika: Mapped[bool | None]
    Google_Analytics: Mapped[bool | None]
    Sketch: Mapped[bool | None]
    Fontjoy: Mapped[bool | None]
    SQLAlchemy: Mapped[bool | None]
    PostgreSQL: Mapped[bool | None]
    Git: Mapped[bool | None]
    Docker: Mapped[bool | None]
    Django: Mapped[bool | None]
  

# for using in ORM mod

metadata_obj = MetaData()

interns_table = Table(
    "interns",
    metadata_obj,
    Column("id", String, primary_key=True),
    Column("email", String),
    Column("name", String),
    Column("role", String),
    Column("internship", String),
    Column("start_date", Date), 
    Column("end_date", Date),
    Column("notes", String),
    schema="cloveri"    
)

grades_table = Table(
    "grades",
    metadata_obj,
    Column("id", String, primary_key=True),
    Column("ai", Float),
    Column("programming", Float),
    Column("architecture", Float),
    Column("project_management", Float),
    Column("communication", Float),
    Column("personnel_management", Float),
    Column("information_management", Float),
    Column("infrastructure", Float),
    Column("data_management", Float),
    Column("visual", Float),
    Column("ux_ui", Float),
    Column("seo", Float),
    Column("typografy", Float),
    Column("skill18", Float),
    Column("skill19", Float),
    Column("skill20", Float),
    schema="cloveri"    
)

tools_table = Table(
    "tools",
    metadata_obj,
    Column("role", String, primary_key=True),
    Column("internship", String),
    Column("Pycaret", Boolean),
    Column("Random_Forest", Boolean),
    Column("Anomaly_Detеction", Boolean),
    Column("Gradient_Boosting", Boolean),
    Column("Cluster_analysis", Boolean),
    Column("K_fold", Boolean),
    Column("Optuna", Boolean),
    Column("Shap", Boolean),
    Column("Tsfresh", Boolean),
    Column("Sklearn_feature_selection", Boolean),
    Column("imblearn", Boolean),
    Column("Streamlit", Boolean),
    Column("tool13", Boolean),
    Column("skill19", Boolean),
    Column("skill20", Boolean),
    Column("skill21", Boolean),
    Column("skill22", Boolean),
    Column("skill23", Boolean),
    Column("skill24", Boolean),
    Column("skill25", Boolean),
    Column("skill26", Boolean),
    Column("skill27", Boolean),
    Column("skill28", Boolean),
    Column("skill29", Boolean),
    Column("skill30", Boolean),
    schema="cloveri"    
)