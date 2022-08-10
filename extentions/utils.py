from . import jalali
from django.utils import timezone

def jalali_converter(time):
    jmonths = ["فروردين", "ارديبهشت", "خرداد", "تير", "مرداد", "شهريور", "مهر", "آبان", "آذر", "دي", "بهمن", "اسفند"]
    time = timezone.localtime(time)
    time_to_str = "{},{},{}".format(time.year, time.month, time.day) 
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    month_persian = jmonths[time_to_tuple[1]-1]

    output = "{} {} {}, ساعت {}:{}".format(
        time_to_tuple[2],
        month_persian,
        time_to_tuple[0],
        time.hour,
        time.minute
    )

    return output