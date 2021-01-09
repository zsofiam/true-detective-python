def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def is_two_digit(number):
    if len(str(number)) == 2:
        return True
    else:
        return False


def is_twodigit_odd(number):
    if is_even(number):
        return False
    else:
        if not is_two_digit(number):
            return False
        else:
            return True


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    pass


def is_leap_year(year):
    if not year % 4 == 0:
        return False
    else:
        if year % 400 == 0:
            return True
        else:
            if year % 100 == 0:
                return False
            else:
                return True


def is_sunday(day, weekday_of_first):
    pass


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    pass


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    pass


if __name__ == "__main__":
    print(is_leap_year(2010))

