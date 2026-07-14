RED_FLAGS = ["chest pain", "dizzy", "faint", "shortness of breath"]

def check_red_flags(text):
    txt = text.lower()
    return any(flag in txt for flag in RED_FLAGS)
