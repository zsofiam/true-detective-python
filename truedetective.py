import whatif


def is_twodigit_odd(number):
    if not whatif.is_even(number) and whatif.is_two_digit(number):
        return True
    else:
        return False


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    has = False
    if sudo_mode:
        has = True
    elif writable_by_others:
        has = True
    elif user == file_owner and writable_by_owner:
        has = True
    elif file_group in users_groups and writable_by_group:
        has = True
    return has


def is_leap_year(year):
    result = False
    if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        result = True
    return result


def is_sunday(day, weekday_of_first):
    result = False
    weekdays = ["M", "T", "W", "Th", "F", "Sa", "Su"]
    day_index = weekdays.index(weekday_of_first)
    index_of_searched_day = (day + day_index) % 7
    if index_of_searched_day == 6:
        result = True
    return result


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    should_bring = False
    if rains and wind_scale < 7:
        should_bring = True
    elif not rains and strong_sunshine and wind_scale < 7:
        should_bring = True
    elif not rains and cloudy and wind_scale < 7 and (red_sky or strong_flower_smell or spiders_down or lying_cattle):
        should_bring = True
    else:
        should_bring = False
    return should_bring


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    should_take = False
    if want_to and not trouble_sleeping and not after_4pm and not at_work and have_30m:
        should_take = True
    elif want_to and not trouble_sleeping and not after_4pm and not at_work and not have_30m and have_10m:
        should_take = True
    elif want_to and not trouble_sleeping and not after_4pm and at_work and not mad_boss and have_30m:
        should_take = True
    elif want_to and not trouble_sleeping and not after_4pm and at_work and not mad_boss and not have_30m and have_10m:
        should_take = True
    return should_take


if __name__ == "__main__":
    print(has_access(42, [142, 143], 11, True, 10, True, True, False)) #is True
    print(has_access(42, [142, 143], 11, True, 10, True, False, True)) #is True
    print(has_access(42, [142, 143], 11, True, 10, True, False, False)) #is False
    print(has_access(42, [142, 143], 11, True, 143, True, False, False)) #is True
    print(has_access(42, [142, 143], 11, True, 143, False, False, False)) #is False
    print(has_access(42, [142, 143], 11, True, 143, False, False, True)) #is True
    print(has_access(42, [142, 143], 42, True, 10, False, False, False)) #is True
    print(has_access(42, [142, 143], 42, False, 10, False, False, False)) #is False
    print(has_access(42, [142, 143], 42, False, 10, False, False, True)) #is True
   