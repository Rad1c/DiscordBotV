from profanityfilter import ProfanityFilter

pf = ProfanityFilter()


def filter_message(message):
    if not message:
        return ""
    return pf.censor(message)
