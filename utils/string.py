import random
import string


def random_string(length=5, chars=string.ascii_lowercase + string.digits):
    """
    Generate the random string
    :param length: the length of the string generated
    :param chars: chars that are used in string generation
    :return: string
    """
    return ''.join((random.choice(chars) for x in range(length)))
