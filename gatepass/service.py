from sqlalchemy.orm import Session
from models import GatePass

def save_qr(db: Session, qr_token, flat, block, valid_from, valid_until):
    gatepass = GatePass(qr_token = qr_toke, flat = flat, block = block, valid_from = valid_from, valid_until = valid_until)
    db.add(gatepass)
    db.commit()
    db.refresh(gatepass)
    return gatepass.pass_id

def generate_qr():
    pass