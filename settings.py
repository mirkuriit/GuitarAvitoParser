from stypes import Stypes


def get_sort_by(sort_by: str) -> int:
    match sort_by:
        case Stypes.DATE:
            return 104
        case Stypes.CHEAPER:
            return 1
        case Stypes.MORE_EXPENSIVE:
            return 2


def get_new_guitar(is_new) -> str:
    if is_new:
        return "ASgBAQICAUTEAsYKAUCEvQ0UrtI0"
    else:
        return "ASgBAQICAUTEAsYKAUCEvQ0UsNI0"


class Settings:
    def __init__(self, sort_by, city, is_new, q):
        self.q: str = q
        self.sort_by: int = get_sort_by(sort_by)
        self.city: str = city
        self.new_guitar: str = get_new_guitar(is_new)



