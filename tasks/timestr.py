__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    days = seconds // 86400
    hours = seconds % 86400 // 3600
    mins = seconds % 3600 // 60
    sec = seconds - days * 86400 - hours * 3600 - mins * 60

    if days:
        return f'{days:02}d{hours:02}h{mins:02}m{sec:02}s'
    if hours:
        return f'{hours:02}h{mins:02}m{sec:02}s'
    if mins:
        return f'{mins:02}m{sec:02}s'
    return f'{sec:02}s'




