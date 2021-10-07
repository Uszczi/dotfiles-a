class Object(object):
    pass


def str_formater_with_const_width(prefix=" ", size=12):
    def format_(value):
        suffix = " " * (size - len(value))
        return prefix + value + suffix

    fmt = Object()
    fmt.format = format_
    return fmt
