from sqlalchemy.orm import Session
from database.models import GatePass
import qrcode
import uuid
import os

def save_qr(db: Session, qr_token, block, flat_number, valid_from, valid_until):
    gatepass = GatePass(
        qr_token=qr_token,
        block=block,
        flat_number=flat_number,
        valid_from=valid_from,
        valid_until=valid_until
    )
    db.add(gatepass)
    db.commit()
    db.refresh(gatepass)
    return gatepass.pass_id

def generate_qr(db: Session, block, flat_number, valid_from, valid_until):
    qr_token = str(uuid.uuid4())

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_token)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    os.makedirs("qr_codes", exist_ok=True)
    file_name = f"{qr_token}.png"
    file_path = f"qr_codes/{file_name}"
    img.save(file_path)

    pass_id = save_qr(db, qr_token, block, flat_number, valid_from, valid_until)

    return {
        "pass_id": pass_id,
        "block": block,
        "flat_number": flat_number,
        "valid_from": valid_from.isoformat(),
        "valid_until": valid_until.isoformat(),
        "qr_url": f"http://127.0.0.1:8000/qr_codes/{file_name}"
    }


def update_gatepass(db: Session, pass_id, block, flat_number, valid_from, valid_until):
    gatepass = db.query(GatePass).filter(GatePass.pass_id == pass_id).first()
    if gatepass:
        gatepass.block = block
        gatepass.flat_number = flat_number
        gatepass.valid_from = valid_from
        gatepass.valid_until = valid_until
        db.commit()
        db.refresh(gatepass)
    return gatepass

def get_gatepass_by_id(db: Session, pass_id: int):
    return db.query(GatePass).filter(GatePass.pass_id == pass_id).first()

def get_gatepasses_by_flat(db: Session, block: str, flat_number: str):
    return db.query(GatePass).filter(
        GatePass.block == block, GatePass.flat_number == flat_number
    ).all()
