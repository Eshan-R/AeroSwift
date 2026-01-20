from datetime import datetime, timezone
from flask_login import current_user
from app.models.audit_log import AuditLog
from app.extensions import db
from flask import request, session

def log_action(action, user_id=None, email=None, ip_address=None):
    final_user_id = user_id or (current_user.id if current_user.is_authenticated else None)

    log = AuditLog(
        user_id = final_user_id,
        action = action,
        ip_address = request.remote_addr,
        timestamp = datetime.now(timezone.utc)
    )

    db.session.add(log)
    db.session.commit()