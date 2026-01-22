from sqlalchemy.orm import Session
from database.models import GatePass
import qrcode
import uuid
import io
import base64

def save_qr(db: Session, qr_token, block, flat_number, valid_from, valid_until, qr_image_bytes):
    gatepass = GatePass(
        qr_token=qr_token,
        block=block,
        flat_number=flat_number,
        valid_from=valid_from,
        valid_until=valid_until,
        qr_image=qr_image_bytes  # Store QR as bytes in DB
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

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="PNG")
    img_bytes = img_byte_arr.getvalue()

    pass_id = save_qr(db, qr_token, block, flat_number, valid_from, valid_until, img_bytes)

    qr_base64 = base64.b64encode(img_bytes).decode("utf-8")  # convert to base64

    return {
        "pass_id": pass_id,
        "block": block,
        "flat_number": flat_number,
        "valid_from": valid_from.isoformat(),
        "valid_until": valid_until.isoformat(),
        "qr_token": qr_token,
        "qr_url": f"data:image/png;base64,{qr_base64}"  # React can use this directly
    }

def update_gatepass(db: Session, pass_id, block, flat_number, valid_from, valid_until, qr_image_bytes=None):
    gatepass = db.query(GatePass).filter(GatePass.pass_id == pass_id).first()
    if gatepass:
        gatepass.block = block
        gatepass.flat_number = flat_number
        gatepass.valid_from = valid_from
        gatepass.valid_until = valid_until
        if qr_image_bytes:
            gatepass.qr_image = qr_image_bytes
        db.commit()
        db.refresh(gatepass)
    return gatepass

def get_gatepass_by_id(db: Session, pass_id: int):
    return db.query(GatePass).filter(GatePass.pass_id == pass_id).first()

def get_gatepasses_by_flat(db: Session, block: str, flat_number: str):
    return db.query(GatePass).filter(
        GatePass.block == block, GatePass.flat_number == flat_number
    ).all()
