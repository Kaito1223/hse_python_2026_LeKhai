from message_predictor import predict_message_mood

assert predict_message_mood("Чапаев и пустота") == "отл"
assert predict_message_mood("Чапаев и пустота", 0.8, 0.99) == "норм"
assert predict_message_mood("Вулкан") == "неуд"
