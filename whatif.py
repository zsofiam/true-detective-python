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
    if sudo_mode:
        return True
    else:
        if writable_by_others:
            return True
        else:
            if user == file_owner:
                if writable_by_owner:
                    return True
            if file_group in users_groups:
                if writable_by_group:
                    return True
    return False 


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
    weekdays = ["M", "T", "W", "Th", "F", "Sa", "Su"]
    day_index = weekdays.index(weekday_of_first)
    index_of_searched_day = (day + day_index) % 7
    if not index_of_searched_day == 6:
        return False
    else:
        return True
    

def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    if rains:
        if wind_scale >= 7:
            return False
        else:
            return True
    else:
        if cloudy:
            if wind_scale < 7:
                if red_sky:
                    return True
                if strong_flower_smell:
                    return True
                if spiders_down:
                    return True
                if lying_cattle:
                    return True
        else:
            if strong_sunshine:
                if wind_scale < 7:
                    return True
                else:
                    return False
            else:
                return False
        return False


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    if want_to:
        if trouble_sleeping:
            return False
        else:
            if after_4pm:
                return False
            else:
                if at_work:
                    if mad_boss:
                        return False
                    else:
                        if have_30m:
                            return True
                        else:
                            if have_10m:
                                return True
                            else:
                                return False
                else:
                    if have_30m:
                        return True
                    else:
                        if have_10m:
                            return True
                        else:
                            return False
    else:
        return False


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



