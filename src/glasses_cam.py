from detect import mayne, parse_opt


def camera(certainty):
    opt = parse_opt()
    certainty_score = mayne(opt, certainty)
