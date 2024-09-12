def isSanDuan(data):
    if len(data) != 3:
        return False
    if str(data[0]).startswith(">") == False or str(data[2]).startswith("==") == False:
        return False
    if validateTime(str(data[1])) == False:
        return False


def validateTime(date_text):
    date_text = date_text[1:].strip()
    import datetime
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return False


def write2_file(content, filename):
    with open(filename, 'a') as f:
        f.write(content)
