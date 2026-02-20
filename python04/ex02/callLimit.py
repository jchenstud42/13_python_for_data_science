RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def callLimit(limit: int):
    """Takes as argument a call limit of another function
    and blocks its execution above a limit.
    Here : receives the limit"""
    if not isinstance(limit, (int)):
        print(f"{RED}Error: arg must be an int{RESET}")
        return lambda: None

    count = 0

    def callLimiter(function):
        """Receives the decorated function"""

        def limit_function(*args: any, **kwds: any):
            """Counts the number of time it was called,
            and blocks if we are reaching the limit"""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"{RED}Error: {function} call too many times{RESET}")
                return None

        return limit_function

    return callLimiter


def main():
    try:

        @callLimit(3)
        def f():
            print("f()")

        # equivalent de :
        # f = callLimit(3)(f)

        @callLimit(1)
        def g():
            print("g()")

        for i in range(3):
            f()
            g()

    except RuntimeError as error:
        print(f"{RED}Error: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------


if __name__ == "__main__":
    main()
