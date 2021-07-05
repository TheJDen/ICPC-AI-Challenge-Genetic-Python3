import unittest
import game
import jflow
default_width, default_height = 7600, 4200

# def has_x_and_y(vec):
#     return hasattr(vec, 'x') and hasattr(vec, 'y')
def has_x_and_y(vec):
    return hasattr(vec, 'x') and hasattr(vec, 'y')

class TestShip(unittest.TestCase):

    def setUp(self):
        self.player = game.Ship([2,3], 90.0)

    def test_has_pos(self):
        self.assertTrue(hasattr(self.player, "pos"))
        pos = self.player.pos
        self.assertTrue(has_x_and_y(pos))

    def test_has_bearing(self):
        self.assertTrue(hasattr(self.player, "bearing"))

    # def test_has_vel(self):
    #     self.assertTrue(hasattr(self.player, "vel"))
    #     vel = self.player.vel
    #     self.assertTrue(has_x_and_y(vel))

    def test_defaults_to_origin(self):
        player = game.Ship()
        self.assertTrue(hasattr(player, "pos"))
        self.assertEqual(player.pos.x, 0)
        self.assertEqual(player.pos.y, 0)

    def test_defaults_to_upright(self):
        player = game.Ship()
        self.assertTrue(hasattr(player, "bearing"))
        self.assertEqual(player.bearing, 90.0)

    def test_maintains_pos(self):
        self.assertEqual(self.player.pos.x, 2)
        self.assertEqual(self.player.pos.y, 3)
        self.player.pos = [7,9]
        self.test_has_pos()
        self.assertEqual(self.player.pos.x, 7)
        self.assertEqual(self.player.pos.y, 9)

class TestArtifact(unittest.TestCase):

    def setUp(self):
        self.artifact = game.Artifact([2,3])

    def test_has_pos(self):
        self.assertTrue(hasattr(self.artifact, "pos"))
        pos = self.artifact.pos
        self.assertTrue(has_x_and_y(pos))

    def test_maintains_pos(self):
        self.assertEqual(self.artifact.pos.x, 2)
        self.assertEqual(self.artifact.pos.y, 3)
        self.artifact.pos = [7,9]
        self.test_has_pos()
        self.assertEqual(self.artifact.pos.x, 7)
        self.assertEqual(self.artifact.pos.y, 9)

    # def test_maintains_vel(self):
    #     self.assertEqual(self.player.vel.x, 0)
    #     self.assertEqual(self.player.vel.y, 0)
    #     self.player.pos = [7,9]
    #     self.assertEqual(self.player.vel.x, 5)
    #     self.assertEqual(self.player.vel.y, 6)

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = game.Player()

    def test_has_perceptron(self):
        self.assertTrue(hasattr(self.player, "perceptron"))

    def test_defaults_to_test_outputs(self):
        input = [1, 2, 3]
        output = self.player.perceptron([1,2,3])
        cmd = "".join((str(val) for val in output))
        self.assertEqual(cmd, "110001")

    def test_has_ship(self):
        self.assertTrue(hasattr(self.player, "ship"))
        self.assertTrue(hasattr(self.player.ship, "pos"))
        self.assertTrue(has_x_and_y(self.player.ship.pos))
        
    

    # def test_has_vel(self):
    #     self.assertTrue(hasattr(self.player, "vel"))
    #     vel = self.player.vel
    #     self.assertTrue(has_x_and_y(vel))

    # def test_defaults_to_origin(self):
    #     player = game.Ship()
    #     self.assertTrue(hasattr(player, "pos"))
    #     self.assertEqual(player.pos.x, 0)
    #     self.assertEqual(player.pos.y, 0)

    # def test_defaults_to_upright(self):
    #     player = game.Ship()
    #     self.assertTrue(hasattr(player, "bearing"))
    #     self.assertEqual(player.bearing, 90.0)

    # def test_maintains_pos(self):
    #     self.assertEqual(self.player.pos.x, 2)
    #     self.assertEqual(self.player.pos.y, 3)
    #     self.player.pos = [7,9]
    #     self.test_has_pos()
    #     self.assertEqual(self.player.pos.x, 7)
    #     self.assertEqual(self.player.pos.y, 9)

class TestWorld(unittest.TestCase):

    def setUp(self):
        self.player = game.Player()

    def test_has_width(self):
        self.world = game.World(self.player)
        self.assertTrue(hasattr(self.world, "width"))
        self.assertEqual(self.world.width, default_width)

    def test_has_height(self):
        self.world = game.World(self.player)
        self.assertTrue(hasattr(self.world, "height"))
        self.assertEqual(self.world.height, default_height)

    def test_has_player(self):
        self.world = game.World(self.player)
        self.assertTrue(hasattr(self.world, "player"))

    def test_has_artifact(self):
        self.world = game.World(self.player)
        self.assertTrue(hasattr(self.world, "artifact"))
        self.assertEqual(self.world.artifact, None)
    # def test_has_asteroids(self):
    #     self.world = game.World(self.player)
    #     self.assertTrue(hasattr(self.world, "asteroids"))
    #     self.assertEqual(self.world.asteroids, [])

    def test_updates(self):
        self.world = game.World(self.player)
        state = { "artfPos": [-3286.76806640625, -284.64599609375],
                "astIds": [3], "astNum": 1,
                "astPos": [[2936.709716796875, -1737.310546875]],
                "astSizes": [49], "currentRound": 1, "currentScore": 0,
                "currentTime": 4.182635307312012, "gameOver": False,
                "lives": 3,
                "shipPos": [-2344.286376953125,-122.93001556396484],
                "shipR": 183.00173950195312,
                }
        self.world.update(state)
        artifact = self.world.artifact
        ship = self.world.player.ship
        self.assertEqual(artifact.pos.x, state["artfPos"][0])
        self.assertEqual(artifact.pos.y, state["artfPos"][1])
        self.assertEqual(ship.pos.x, state["shipPos"][0])
        self.assertEqual(ship.pos.y, state["shipPos"][1])
        self.assertEqual(ship.bearing, state["shipR"])
        # self.assertEqual(len(self.world.asteroids), 1)

    def test_toroidal_difference(self):
        self.world = game.World(self.player)
        state = { "artfPos": [-3286.76806640625, -284.64599609375],
                "astIds": [3], "astNum": 1,
                "astPos": [[2936.709716796875, -1737.310546875]],
                "astSizes": [49], "currentRound": 1, "currentScore": 0,
                "currentTime": 4.182635307312012, "gameOver": False,
                "lives": 3,
                "shipPos": [-2344.286376953125,-122.93001556396484],
                "shipR": 183.00173950195312,
                }
        self.world.update(state)
        displacement = self.world.min_displacements_to(self.world.artifact)
        self.assertAlmostEqual(displacement.x, -942.481689453)
        self.assertAlmostEqual(displacement.y, -161.71598053)
        state = {"artfPos": [-3000.0, -1000.0],
                "shipPos": [3000.0,1000.0],
                "shipR": 90.0}
        self.world.update(state)
        displacement = self.world.min_displacements_to(self.world.artifact)
        self.assertEqual(displacement.x, 1600.0)
        self.assertEqual(displacement.y, -2000.0)


if __name__ == "__main__":
    unittest.main()
#     def test_maintains_pos(self):
#         self.assertEqual(self.player.pos.x, 2)
#         self.assertEqual(self.player.pos.y, 3)
#         self.player.pos = [7,9]
#         self.test_has_pos()
#         self.assertEqual(self.player.pos.x, 7)
#         self.assertEqual(self.player.pos.y, 9)
    
#     def test_has_bearing(self):
#         self.assertTrue(hasattr(self.player, "bearing"))

#     def test_has_vel(self):
#         self.assertTrue(hasattr(self.player, "vel"))
#         vel = self.player.vel
#         self.assertTrue(has_x_and_y(vel))

#     def test_maintains_vel(self):
#         self.assertEqual(self.player.vel.x, 0)
#         self.assertEqual(self.player.vel.y, 0)
#         self.player.pos = [7,9]
#         self.assertEqual(self.player.vel.x, 5)
#         self.assertEqual(self.player.vel.y, 6)


# class TestGameState(unittest.TestCase):
    
#     def setUp(self):
#         data = {'artfPos': [-2749.65234375, 1245.014404296875],
#         'astIds': [], 'astNum': 0, 'astPos': [], 'astSizes': [],
#         'bulIds': [], 'bulNum': 0, 'bulPos': [], 'bulSrc': [],
#         'currentRound': 1, 'currentScore': 5000.0, 'currentTime': 540.702392578125, 
#         'lives': 3, 'magic_num2': 3490578157,
#         'shipPos': [0.0, 0.0], 'shipR': 90.0,
#         'ufoIds': [], 'ufoNum': 0, 'ufoPos': [], 'ufoSizes': []}
#         self.game = planetoids.GameState(data)


#     def test_has_player(self):
#         self.assertTrue(hasattr(self.game, 'player'))
#         self.assertTrue(isinstance(self.game.player, planetoids.Player))

#     def test_has_artifact_pos(self):
#         self.assertTrue(hasattr(self.game, 'artifact_pos'))
#         artPos = self.game.artifact_pos
#         self.assertTrue(has_x_and_y(artPos))
