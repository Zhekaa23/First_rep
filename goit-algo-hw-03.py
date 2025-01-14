import datetime
import random
import re

# cntrl + k + u - розкоментувати вибраний текст , cntrl + k + с - закоментувати
# Перше завдання


def get_days_from_today(date: str) -> int:
    input_date = datetime.datetime.strptime(date, "%Y.%m.%d").date()
    current_date = datetime.date.today()
    result = current_date - input_date
    return result.days


try:
    our_date = input("Enter your date in format Year/month/day like 2000.11.21 - ")
    print(
        f"The difference betwen {datetime.date.today} and {our_date} is - {get_days_from_today(our_date)} day/s"
    )
except ValueError:
    print("Неправильний формат дати , заупстіть програму ще раз)")


# Друге завдання


# def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
#     if not (min >= 0 and min < max <= 1000 and min <= quantity <= max):
#         print("Incorrect values")
#         return []
#     else:
#         nums = set()
#         while len(nums) != quantity:
#             nums.add(random.randint(min, max))
#     return list(nums)


# lottery_numbers = get_numbers_ticket(1, 49, 51)
# print("Ваші лотерейні числа:", lottery_numbers)


# Третє завдання


# def normalize_phone(phone_number: str) -> str:
#     new_number = re.sub(r"[^\d+]", "", phone_number)
#     if not new_number.startswith("+"):
#         if new_number.startswith("38"):
#             new_number = "+" + new_number
#         else:
#             new_number = "+38" + new_number
#     return new_number


# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
