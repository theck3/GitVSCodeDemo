# condition : we sleep in if it is not a weekday, or we're on vacation. Return true if we sleep in
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False