import operator
import random
class Matrix:

    def __init__(self, format):
        self.rows = [[entry for entry in row] for row in format]
    
    def __str__(self):
        return str(self.rows)

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, i):
        return self.rows[i]

    def __iter__(self):
        return iter(self.rows)

    def __matmul__(self, other):
        def inner_prod (A, B):
            return sum(map(operator.mul, A, B))
        return Matrix((inner_prod(row, col) for col in zip(*other)) for row in self)

    def __mul__(self, vector):
        def inner_prod (A, B):
            return sum(map(operator.mul, A, B))
        return [inner_prod(row, vector) for row in self]

# class Layer:

#     def __init__(self, length, input_dim=None, activation=lambda x: x):
#         self.values = Matrix(([0] for _ in range(length)))
#         self.activation = activation
#         if input_dim:
#             self.weights = Matrix(((random.uniform(-1, 1) for _ in range(input_dim)) for _ in self.pointers))


#     def __call__(self, prev_layer):
#         self.weights = Matrix(((random.uniform(-1, 1) for _ in prev_layer) for _ in self.pointers))
#         return self

#     @property
#     def activation(self):
#         return self._activation

#     @activation.setter
#     def activation(self, func):
#         if callable(func): self._activation = func
#         else: self._activation = lambda x: x

#     def activate(self):
#         for pointer in self.pointers:
#             for datum in pointer:
#                 pointer[0] = self._activation(datum)

#     def __str__(self):
#         return str(self.pointers)

#     def __len__(self):
#         return len(self.pointers)

#     def __getitem__(self, i):
#         return self.pointers[i]

#     def __iter__(self):
#         return iter(self.pointers)

class Layer:

    def __init__(self, length, input_dim=None, activation=lambda x: x):
        self.values = [0]*length
        self.activation = activation
        if input_dim:
            self.weights = Matrix(((random.uniform(-1, 1) for _ in range(input_dim)) for _ in self.values))


    def __call__(self, prev_layer):
        self.weights = Matrix(((random.uniform(-1, 1) for _ in prev_layer) for _ in self.values))
        return self

    @property
    def activation(self):
        return self._activation

    @activation.setter
    def activation(self, func):
        if callable(func): self._activation = func
        else: self._activation = lambda x: x

    def activate(self):
        self.values = [self._activation(val) for val in self.values]

    def __str__(self):
        return str(self.values)

    def __len__(self):
        return len(self.values)

    # def __getitem__(self, i):
    #     return self.values[i]

    def __iter__(self):
        return iter(self.values)

# class Network:

#     def __init__(self, layers):
#         self.layers = layers
#         iter_layers = iter(layers)
#         prev_layer = next(iter_layers)
#         for layer in iter_layers:
#             layer(prev_layer)
#             prev_layer = layer

#     def __getitem__(self, i):
#         return self.layers[i]

#     def __iter__(self):
#         return iter(self.layers)

#     def process(self, input):
#         prev = [[datum] for datum in input]
#         for layer in self.layers:
#             layer.pointers = layer.weights @ prev
#             layer.activate()
#             prev = layer.pointers
#         return self.layers[-1]

#     def __repr__(self):
#         return str([str(layer) for layer in self.layers])

class Network:

    def __init__(self, layers):
        self.layers = layers
        iter_layers = iter(layers)
        prev_layer = next(iter_layers)
        for layer in iter_layers:
            layer(prev_layer)
            prev_layer = layer

    def __getitem__(self, i):
        return self.layers[i]

    def __iter__(self):
        return iter(self.layers)

    # def process(self, input):
    #     prev = input
    #     for layer in self.layers:
    #         layer.values = layer.weights * prev
    #         layer.activate()
    #         prev = layer.values
    #     return self.layers[-1]

    def __call__(self, input):
        prev = input
        for layer in self.layers:
            layer.values = layer.weights * prev
            layer.activate()
            prev = layer.values
        return self.layers[-1]

    def __repr__(self):
        return str([str(layer) for layer in self.layers])