'''Matplotlib formatter.'''
from typing import Tuple
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from typing import List

class Format:
    '''Applies a default Matplotlib format to plt.rcParams.'''

    def __init__(self, font_paths: List[str] = None,
                 font_serif: List[str] = ['CMU Serif', 'Times New Roman', 'FreeSerif']):
        self.font_paths = font_paths
        self.font_serif = font_serif
    
    def rcUpdate(self, font_size: int = 15, font_family: str = 'serif',
                   font_weight: str = 'light', math_font: str ='cm') -> None:
        if self.font_paths:
            for font in self.font_paths:
                Format.addFont(font)
        
        rc_update = {'font.size': font_size, 'font.family': font_family,
				 'font.serif': self.font_serif, 'font.weight': font_weight,
                 'mathtext.fontset': math_font}
        plt.rcParams.update(rc_update)

    @staticmethod
    def addFont(font_path: str) -> str:
        try:
            font_manager.fontManager.addfont(font_path)
            prop = font_manager.FontProperties(fname=font_path)
        except FileNotFoundError:
            print(f'WARNING: Font {font_path} not found.')


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
