def get_coordinate(record):
    return record[1]
def convert_coordinate(coordinate):
    return tuple(coordinate)
def compare_records(azara_record, rui_record):
    return tuple(azara_record[1]) == rui_record[1]
def create_record(azara_record, rui_record):
    return azara_record + rui_record if compare_records(azara_record, rui_record) else 'not a match'
def clean_up(combined_record_group):
    valore = tuple(tuple([i[0]])+i[2:] for i in combined_record_group)
    report = "\n".join(str(record) for record in valore) + "\n"
    return report