from django.conf import settings

def calculate_batch_size(data_len):
    if data_len<100:
        return None
    num_batches=getattr(settings, 'NUM_BATCHES',4)
    return data_len // num_batches