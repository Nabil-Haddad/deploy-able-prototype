from sqlalchemy import Column, Integer, String, Float, Date
from db.database import Base

class ProductionModel(Base):
    __tablename__ = "production_metrics"

    # Unique identifier for each row
    id = Column(Integer, primary_key=True, index=True)
    
    # Core columns matching your schema (indexed for fast searching)
    date = Column(Date, index=True, nullable=False)
    production_line = Column(String(50), index=True, nullable=False)
    shift = Column(String(50), nullable=False)
    
    # Numeric values
    units_planned = Column(Integer, default=0, nullable=False)
    units_produced = Column(Integer, default=0, nullable=False)
    defective_units = Column(Integer, default=0, nullable=False)
    downtime_minutes = Column(Integer, default=0.0, nullable=False)