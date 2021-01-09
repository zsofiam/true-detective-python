import whatif


def is_twodigit_odd(number):
    if not whatif.is_even(number) and whatif.is_two_digit(number):
        return True
    else:
        return False


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    pass


def is_leap_year(year):
    result = False
    if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        result = True
    return result


def is_sunday(day, weekday_of_first):
    pass


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    pass


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    pass

if __name__ == "__main__":
    print(is_leap_year(1988))
   