import unittest
import planetoids

def has_x_and_y(vec):
    return hasattr(vec, 'x') and hasattr(vec, 'y')

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = planetoids.Player([2,3], 90.0)

    def test_has_pos(self):
        self.assertTrue(hasattr(self.player, "pos"))
        pos = self.player.pos
        self.assertTrue(has_x_and_y(pos))

    def test_maintains_pos(self):
        self.assertEqual(self.player.pos.x, 2)
        self.assertEqual(self.player.pos.y, 3)
        self.player.pos = [7,9]
        self.test_has_pos()
        self.assertEqual(self.player.pos.x, 7)
        self.assertEqual(self.player.pos.y, 9)
    
    def test_has_bearing(self):
        self.assertTrue(hasattr(self.player, "bearing"))

    def test_has_vel(self):
        self.assertTrue(hasattr(self.player, "vel"))
        vel = self.player.vel
        self.assertTrue(has_x_and_y(vel))

    def test_maintains_vel(self):
        self.assertEqual(self.player.vel.x, 0)
        self.assertEqual(self.player.vel.y, 0)
        self.player.pos = [7,9]
        self.assertEqual(self.player.vel.x, 5)
        self.assertEqual(self.player.vel.y, 6)


class TestGameState(unittest.TestCase):
    
    def setUp(self):
        data = {'artfPos': [-2749.65234375, 1245.014404296875],
        'astIds': [], 'astNum': 0, 'astPos': [], 'astSizes': [],
        'bulIds': [], 'bulNum': 0, 'bulPos': [], 'bulSrc': [],
        'currentRound': 1, 'currentScore': 5000.0, 'currentTime': 540.702392578125, 
        'lives': 3, 'magic_num2': 3490578157,
        'shipPos': [0.0, 0.0], 'shipR': 90.0,
        'ufoIds': [], 'ufoNum': 0, 'ufoPos': [], 'ufoSizes': []}
        self.game = planetoids.GameState(data)


    def test_has_player(self):
        self.assertTrue(hasattr(self.game, 'player'))
        self.assertTrue(isinstance(self.game.player, planetoids.Player))

    def test_has_artifact_pos(self):
        self.assertTrue(hasattr(self.game, 'artifact_pos'))
        artPos = self.game.artifact_pos
        self.assertTrue(has_x_and_y(artPos))

    #TODO change data
    # def test_update(self):
    #     data = {'artfPos': [-2749.65234375, 1245.014404296875],
    #     'astIds': [], 'astNum': 0, 'astPos': [], 'astSizes': [],
    #     'bulIds': [], 'bulNum': 0, 'bulPos': [], 'bulSrc': [],
    #     'currentRound': 1, 'currentScore': 5000.0, 'currentTime': 540.702392578125, 
    #     'lives': 3, 'magic_num2': 3490578157,
    #     'shipPos': [0.0, 0.0], 'shipR': 90.0,
    #     'ufoIds': [], 'ufoNum': 0, 'ufoPos': [], 'ufoSizes': []}
    #     game = planetoids.Game(data)
    #     self.assertTrue(isinstance(game.agent, planetoids.Player))



    # def has_vel(self):
    #     self.assertTrue(hasattr(player, "vel"))
    #     vel = player.vel
    #     self.assertTrue(hasattr(vel, 'x'))
    #     self.assertTrue(hasattr(vel, 'y'))

    # def vel_maintains(self):
    #     vel = player.vel
    #     self.assertEqual(vel.x, 0.0)
    #     self.assertTrue(vel.y, 0.0)
    #     player.pos = [7,9]

if __name__ == '__main__':
    unittest.main()
