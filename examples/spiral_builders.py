from builder import AlgebraSpiralBuilder, ConditionalSpiralBuilder

if __name__ == '__main__':
    print(ConditionalSpiralBuilder().build(5), end='\n\n')
    print(AlgebraSpiralBuilder().build(5), end='\n\n')
