class SomeModel:  # pylint: disable=too-few-public-methods
    def __init__(self) -> None:
        pass

    def predict(self, _message: str) -> float:
        return min((len(_message) - 2) / 16, 1.0)


def predict_message_mood(
    message: str,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    score = SomeModel().predict(message)
    if score < bad_thresholds:
        return "неуд"
    if score > good_thresholds:
        return "отл"
    return "норм"
