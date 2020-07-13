from algorithms.stack import ArrayStack


def is_matched(expression: str) -> bool:
    """Return True if all delimiters ate properly match; False oterwise"""
    lefty = "({["
    righty = ")}]"
    S = ArrayStack()
    for character in expression:
        if character in lefty:
            S.push(character)
        elif character in righty:
            if S.is_empty():
                return False
            if righty.index(character) != lefty.index(S.pop()):
                return False
    return S.is_empty()
