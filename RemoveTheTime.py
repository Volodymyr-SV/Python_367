def shorten_to_date(long_date):
    date=""
    for x in long_date:
        if x==",":
            break
        date+=x
    return date