import shortuuid


def short_uuid_generator(
    _len: int = 7
) -> shortuuid.ShortUUID:
    """
    This function return a random shortuuid every time that is called
    """
    return shortuuid.ShortUUID().random(_len)