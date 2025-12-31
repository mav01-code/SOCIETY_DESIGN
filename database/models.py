from sqlalchemy import Column, String, Integer, BigInteger, Enum, CHAR, DateTime, TIMESTAMP
from database.db import Base
from datetime import datetime

class Resident(Base):
    __tablename__ = "residents"

    name = Column(String(100), nullable=False)
    authorization = Column(Enum("Home Owner", "President", "Vice"), nullable=False)
    total_family_members = Column(Integer, nullable=False)
    block = Column(CHAR(1), primary_key=True)
    flat_number = Column(String(10), primary_key=True)


class GatePass(Base):
    __tablename__ = "gatepasses"

    pass_id = Column(BigInteger, primary_key=True, autoincrement=True)
    block = Column(CHAR(1), nullable=False)
    flat_number = Column(String(10), nullable=False)
    qr_token = Column(String(255), unique=True, nullable=False)
    valid_from = Column(DateTime, nullable=False)
    valid_until = Column(DateTime, nullable=False)


class EntryLog(Base):
    __tablename__ = "entry_logs"

    log_id = Column(BigInteger, primary_key=True, autoincrement=True)
    block = Column(CHAR(1))
    flat_number = Column(String(10))
    visitor_name = Column(String(100))
    visitor_type = Column(Enum('ZOMATO','SWIGGY','MAID','DELIVERY','GUEST','MAINTENANCE'))
    pass_mode = Column(Enum('QR','AUTO','INSTANT'))
    status = Column(Enum('ALLOWED','DENIED'))
    scanned_at = Column(TIMESTAMP, default=datetime.utcnow)
