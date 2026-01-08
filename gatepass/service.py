from sqlalchemy.orm import Session
from models import GatePass
import qrcode
import uuid

def save_qr(db: Session, qr_token, flat, block, valid_from, valid_until):
    gatepass = GatePass(qr_token = qr_token, flat = flat, block = block, valid_from = valid_from, valid_until = valid_until)
    db.add(gatepass)
    db.commit()
    db.refresh(gatepass)
    return gatepass.pass_id

def generate_qr(db: Session, flat, block, valid_from, valid_until):
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
    file_path = f"qr_codes/{qr_token}.png"
    img.save(file_path)

    pass_id = save_qr(db, qr_token, flat, block, valid_from, valid_until)

    return pass_id, file_path