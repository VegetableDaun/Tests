def scoreboard(who_ate_what):
    points = {'chickenwings': 5, "hamburgers": 3, "hotdogs": 2}

    for par in who_ate_what:
        for dish, point in points.items():
            par['score'] = par.get('score', 0) + par.get(dish, 0) * point
            if par.get(dish, 0) != 0: del par[dish]

    who_ate_what.sort(key=lambda participant: (-participant['score'], participant['name']))

    return who_ate_what


pt = [{"name": "B", "hamburgers": 4, "hotdogs": 11},
      {"name": "A", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]
print(scoreboard(pt))
