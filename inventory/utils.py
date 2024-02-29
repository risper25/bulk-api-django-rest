def calculate_batch_size(data_len):
    if data_len<100:
        return None
    return data_len // 4