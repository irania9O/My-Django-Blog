from . import jalali
from django.utils import timezone

def persian_number_conventor(input_str):
    numbers = {
        "0": "۰",
        "1": "١",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }
    for english_number, persian_number in numbers.items():
        input_str = input_str.replace(english_number, persian_number)
    
    return input_str

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

    return persian_number_conventor(output)