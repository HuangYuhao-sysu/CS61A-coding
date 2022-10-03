class Baller:
    all_players = []
    def __init__(self, name, has_ball = False):
        self.name = name
        self.has_ball = has_ball
        Baller.all_players.append(self)

    def pass_ball(self, other_player):
        if self.has_ball:
            self.has_ball = False
            other_player.has_ball = True
            return True
        else:
            return False

class BallHog(Baller):
    def pass_ball(self, other_player):
        return False

class TeamBaller(Baller):
    """
    >>> cheerballer = TeamBaller('Thomas', has_ball=True)
    >>> cheerballer.pass_ball(surya)
    Yay!
    True
    >>> cheerballer.pass_ball(surya)
    I don't have the ball
    False
    """
    def pass_ball(self, other_player):
        if self.has_ball:
            print('Yay!')
        else:
            print("I don't have the ball")
        return Baller.pass_ball(self, other_player)

class PingPongTracker:
    def __init__(self):
        self.current = 0
        self.index = 1
        self.add = True

    def next(self):
        if has_seven(self.index):
            self.add = not self.add

        if self.add:
            self.current += 1
        else:
            self.current -= 1

        self.index += 1
        return self.current



