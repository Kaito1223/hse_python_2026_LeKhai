def retry_deco(
    number_of_tries: int = 3,
    expected_exceptions: list[type[Exception]] | None = None,
):
    if number_of_tries < 1:
        raise ValueError("number_of_tries must be at least 1")

    def decorator(func):
        def wrapper(*args, **kwargs):
            tries = 0
            while tries < number_of_tries:
                try:
                    result = func(*args, **kwargs)
                    print(
                        f"run '{func.__name__}', args = {args}, "
                        f"kwargs = {kwargs}, attempt = {tries + 1}, "
                        f"result = {result}."
                    )
                    return result

                except Exception as e:  # pylint: disable=broad-exception-caught
                    if (
                        expected_exceptions is not None
                        and type(e) in expected_exceptions
                    ):
                        print(
                            f"run '{func.__name__}', args = {args}, "
                            f"kwargs = {kwargs}, attempt = {tries + 1}, "
                            f"exception = {e}."
                        )
                        raise

                    print(
                        f"run '{func.__name__}', args = {args}, "
                        f"kwargs = {kwargs}, attempt = {tries + 1}, "
                        f"exception = {e}."
                    )
                    tries += 1
                    if tries == number_of_tries:
                        raise

            raise RuntimeError("Some error")
        return wrapper
    return decorator
