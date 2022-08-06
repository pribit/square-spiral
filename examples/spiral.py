from builder import ConditionalSpiralBuilder
from src.spiral import Spiral


if __name__ == '__main__':
    spiral: Spiral = Spiral(5)
    print(spiral, end='\n\n')
    print(spiral.get_spiral())

    spiral_conditional: Spiral = Spiral(5, builder_cls=ConditionalSpiralBuilder)
    print(spiral_conditional.get_spiral())
