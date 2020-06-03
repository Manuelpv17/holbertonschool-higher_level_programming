#!/usr/bin/python3
"""Only sub class of
    """


def inherits_from(obj, a_class):
    """if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class ; otherwis
    False.

        Arguments:
                obj {[type]} -- Object
                a_class {[type]} -- Class

        Returns:
                Bool -- True if inherits
        """
    return isinstance(obj, a_class) and type(obj) is not a_class
