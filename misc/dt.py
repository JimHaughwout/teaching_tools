from datetime import datetime
import pytz

def isotime_from_str(yyyymmdd, hhmmss):
    """
    Generates and returns IS0-8601 compliant date-time string (in UTC)
    from two input strings:
    - YYYYMMDD
    - HHMMSS

    Returns error if input strings are in invalid
    """
    if len(yyyymmdd) != 8 or len(hhmmss) != 6:
        return "Invalid datetime - Invalid arg lengths for YYYYMMDD = %r, HHMMSS = %r" % (yyyymmdd, hhmmss)

    try:
        year = int(yyyymmdd[0:4])
        mon = int(yyyymmdd[4:6])
        day = int(yyyymmdd[6:8])

        hr = int(hhmmss[0:2])
        mins = int(hhmmss[2:4])
        sec = int(hhmmss[4:6])

        dt = datetime(year, mon, day, hr, mins, sec, tzinfo=pytz.utc)
        return dt.isoformat()

    except ValueError as e:
        return "Invalid datetime - Invalid arg values. YYYYMMDD = %r, HHMMSS = %r: %s" % (yyyymmdd, hhmmss, e)


""" TRY IT OUT AND PRINT RESULTS"""
x = isotime_from_str("150721", "123530") # 2-digit year
y = isotime_from_str("20150721", "1235") # No seconds
z = isotime_from_str("2015A721", "123530") # Letter vs number
a = isotime_from_str("20150721", "123530") # Correct

print x
print y
print z
print a