import unittest
import jflow
import collections

class TestMatrix(unittest.TestCase):

    def test_correct_string(self):
        format = [[1,2],[3,4], [5,6]]
        matrix = jflow.Matrix(format)
        self.assertEqual(str(format), str(matrix))

    def test_is_enumerable(self):
        format = [[1,2],[3,4], [5,6]]
        matrix = jflow.Matrix(format)
        for i, row in enumerate(matrix):
            self.assertEqual(row, format[i])
            self.assertEqual(row, matrix[i])
        
    def test_assigns_in_place(self):
        format = [[1,2],[3,4], [5,6]]
        matrix = jflow.Matrix(format)
        matrix[0][0] = 2
        self.assertNotEqual(matrix.rows[0][0], format[0][0])
        self.assertEqual(matrix.rows[0][0], 2)

    def test_correct_entries(self):
        format = [[1,2],[3,4], [5,6]]
        matrix = jflow.Matrix(format)
        self.assertEqual(len(matrix), len(format))
        for row, format_row in enumerate(format):
            self.assertNotEqual(id(matrix[row]), id(format_row))
            self.assertEqual(len(matrix[row]), len(format_row))
            for col, format_entry in enumerate(format_row):
                self.assertEqual(matrix[row][col], format_entry)

    def test_deep_copies(self):
        format = [[1,2],[3,4], [5,6]]
        matrix = jflow.Matrix(format)
        copy = jflow.Matrix(matrix)
        self.assertEqual(len(matrix), len(copy))
        for row, copy_row in enumerate(copy):
            self.assertNotEqual(id(matrix[row]), id(copy_row))
            self.assertEqual(len(matrix[row]), len(copy_row))
            for col, copy_entry in enumerate(copy_row):
                self.assertEqual(matrix[row][col], copy_entry)


    def test_matmul(self):
        A = jflow.Matrix([[1, 2, 3], [4, 5, 6]])
        B = jflow.Matrix([[7, 8], [9, 10], [11, 12]])
        C = A@B
        self.assertTrue(isinstance(C, jflow.Matrix))
        prod = [[58, 64], [139, 154]]
        for row in range(len(C)):
            for col in range(len(C[row])):
                self.assertEqual(C[row][col], prod[row][col])

    def test_vecmul(self):
        A = jflow.Matrix([[1, 2, 3], [4, 5, 6], [7,8,9], [10, 11, 12]])
        B = [13, 14, 15]
        C = A*B
        prod = [86, 212, 338, 464]
        for row, value in enumerate(C):
            self.assertEqual(value, prod[row])

class TestLayer(unittest.TestCase):

    def test_has_length(self):
        layer = jflow.Layer(10)
        self.assertEqual(len(layer), 10)

    def test_is_enumerable(self):
        layer = jflow.Layer(10)
        for i, val in enumerate(layer):
            self.assertEqual(layer.values[i], val)

    def test_has_activation_func(self):
        layer = jflow.Layer(10)
        self.assertTrue(hasattr(layer, "activation"))
        self.assertTrue(callable(layer.activation))
        layer = jflow.Layer(10, activation=lambda x: x**2)
        self.assertTrue(hasattr(layer, "activation"))
        self.assertTrue(callable(layer.activation))
    
    def test_activation_func_takes_funcs(self):
        layer = jflow.Layer(10, activation="bruh")
        self.assertTrue(callable(layer.activation))
        layer.activation = "bruh"
        self.assertTrue(callable(layer.activation))

    # def test_activate_func(self):
    #     func = lambda x: x**2
    #     layer = jflow.Layer(5, activation=func)
    #     for i, pointer in enumerate(layer):
    #         pointer[0] = i
    #     layer.activate()
    #     for i, pointer in enumerate(layer):
    #         self.assertEqual(pointer[0], func(i))
    
    def test_activate_func(self):
        func = lambda x: x**2
        layer = jflow.Layer(5, activation=func)
        for i, _ in enumerate(layer):
            layer.values[i] = i
        layer.activate()
        for i, val in enumerate(layer):
            self.assertEqual(val, func(i))

    def test_has_weights(self):
        layer = jflow.Layer(2, input_dim = 3)
        self.assertTrue(hasattr(layer, "weights"))
        self.assertEqual(len(layer.weights), 2)
        for input_weights in layer.weights:
            self.assertEqual(len(input_weights), 3)

    def test_establishes_weights(self):
        layer1 = jflow.Layer(2, input_dim = 3)
        layer2 = jflow.Layer(4)(layer1)
        self.assertTrue(hasattr(layer2, "weights"))
        self.assertEqual(len(layer2.weights), 4)
        for input_weights in layer2.weights:
            self.assertEqual(len(input_weights), 2)

# class TestNetwork(unittest.TestCase):

#     # def test_has_length(self):
#     #     model = jflow.Network([
#     #         jflow.Layer(4),
#     #         jflow.Layer(5),
#     #         jflow.Layer(6),
#     #     ])
#     #     self.assertEqual(len(model), 3)

#     def test_is_enumerable(self):
#         network = jflow.Network([
#             jflow.Layer(5, input_dim=4),
#             jflow.Layer(6),
#         ])
#         for i, layer in enumerate(network):
#             self.assertEqual(network[i], layer)

#     def test_builds_implicit_connections(self):
#         network = jflow.Network([
#             jflow.Layer(5, input_dim=4),
#             jflow.Layer(6),
#         ])
#         prev_length = 4
#         for layer in network:
#             for input_weights in layer.weights:
#                 self.assertEqual(len(input_weights), prev_length)
#             prev_length = len(layer)
    
#     def test_actuates_input(self):
#         network = jflow.Network([
#             jflow.Layer(5, input_dim=4),
#             jflow.Layer(6),
#         ])
#         before = [entry[:] for entry in network.layers[-1]]
#         #print(before)
#         input = [4, 2, 9, 6]
#         #print(network)
#         network.process(input)
#         #print(before)
#         #print(network)
#         for i, entry in enumerate(network.layers[-1]):
#             self.assertNotAlmostEqual(before[i][0], entry[0])

#     # def test_is_enumerable(self):
#     #     network = jflow.Network([
#     #         jflow.Layer(4),
#     #         jflow.Layer(5),
#     #         jflow.Layer(6),
#     #     ])
#     #     for i, layer in enumerate(network):
#     #         self.assertEqual(network[i], layer)
class TestNetwork(unittest.TestCase):

    # def test_has_length(self):
    #     model = jflow.Network([
    #         jflow.Layer(4),
    #         jflow.Layer(5),
    #         jflow.Layer(6),
    #     ])
    #     self.assertEqual(len(model), 3)

    def test_is_enumerable(self):
        network = jflow.Network([
            jflow.Layer(5, input_dim=4),
            jflow.Layer(6),
        ])
        for i, layer in enumerate(network):
            self.assertEqual(network[i], layer)

    def test_builds_implicit_connections(self):
        network = jflow.Network([
            jflow.Layer(5, input_dim=4),
            jflow.Layer(6),
        ])
        prev_length = 4
        for layer in network:
            for input_weights in layer.weights:
                self.assertEqual(len(input_weights), prev_length)
            prev_length = len(layer)

    def test_is_input_output_machine(self):
        network = jflow.Network([
            jflow.Layer(5, input_dim=4),
            jflow.Layer(6),
        ])
        before = list(network.layers[-1])
        #print(before)
        input = [4, 2, 9, 6]
        #print(network)
        try: network(input)
        except: self.fail("network should be callable")
        #print(before)
        #print(network)
        for i, entry in enumerate(network.layers[-1]):
            self.assertNotAlmostEqual(before[i], entry)

    # def test_is_enumerable(self):
    #     network = jflow.Network([
    #         jflow.Layer(4),
    #         jflow.Layer(5),
    #         jflow.Layer(6),
    #     ])
    #     for i, layer in enumerate(network):
    #         self.assertEqual(network[i], layer)



if __name__ == '__main__':
    unittest.main()