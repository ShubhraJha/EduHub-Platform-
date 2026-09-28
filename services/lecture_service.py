from db_models.lecture_model import get_lectures


def get_batch_lectures(batch_id):

    return get_lectures(batch_id)