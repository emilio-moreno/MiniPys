'''Matplotlib formatter.'''
from typing import Tuple
import matplotlib.pyplot as plt

class Format:
    '''Applies a default Matplotlib format to plt.rcParams.'''
    
    font_serif = ['Times New Roman', 'FreeSerif']
    
    def rcUpdate(font_size: int = 15, font_family: str = 'serif',
                   math_font: str ='cm') -> None:
        rc_update = {'font.size': font_size, 'font.family': font_family,
				 'font.serif': Format.font_serif,
                 'mathtext.fontset': math_font}
        plt.rcParams.update(rc_update)

class Colors:
    
    def __init__(self, *args: Tuple[str, str]) -> None:
        '''
        Builds color dictionary from *args. *args must be a series of tuple
        containing in zeroth position color name and in first position value.
        Also assings colors as instance attributes.
        '''
        self.colors = dict(list(args))
        for c in args:
            setattr(self, c[0], c[1])
    
    def __getitem__(self, value):
        return self.colors[value]