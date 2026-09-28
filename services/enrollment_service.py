from db_models.enrollment_model import *

def confirm_enrollment(student_id, batch_id, txn_id):

    fee = get_batch_fee(batch_id)

    enrollment_id = insert_enrollment(
        student_id,
        batch_id,
        fee
    )

    insert_payment(
        enrollment_id,
        fee,
        txn_id
    )

    activate_enrollment(enrollment_id)