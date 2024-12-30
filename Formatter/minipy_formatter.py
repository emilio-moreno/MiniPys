'''Matplotlib formatter.'''
from typing import Tuple
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from typing import List
from textwrap import wrap
from colorsys import hls_to_rgb, rgb_to_hls

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
    
    def __init__(self, *args: Tuple[str, str], code_type: str = 'hex') -> None:
        '''
        Builds Color dictionary from *args. *args must be a series of tuple
        containing in zeroth position color name and in the first position
        the color code (hex or RGB). Also assings colors as instance attributes.
        '''
        self.colors = dict(list(args))
        for c in args:
            color = Color(c[1], code_type)
            setattr(self, c[0], color)
    
    def __getitem__(self, value):
        return self.colors[value]


RGB_type = Tuple[int, int, int]
class Color:
    supported_codes = {'hex', 'rgb'}

    @staticmethod
    def check_code(code_type: str) -> None:
        if not code_type in Color.supported_codes:
            raise ValueError(f"Code {code_type} not supported."
                             f"Use a code type from {Color.supported_codes}.")
    
    def __init__(self, code: str | RGB_type,
                 code_type: str = 'hex') -> None:
        Color.check_code(code_type)

        if code_type == 'hex':
            self.hex = code
            self.rgb = Color.hex_to_rgb(code)

        if code_type == 'rgb':
            self.rgb = code
            self.hex = Color.rgb_to_hex(*code)
        self.code_type = code_type

    def dark(self, light: int = -25,
             code_type: str = 'hex') -> str | RGB_type:
        '''Subtracts lightness from HSL value of color. Returns hex or rgb.'''
        return Color.change_lightness(self.rgb, light=light,
                                      code_type=code_type)

    def light(self, light: int = 25,
              code_type: str = 'hex') -> str | RGB_type:
        '''Adds lightness from HSL value of color. Returns hex or rgb.'''
        return Color.change_lightness(self.rgb, light=light,
                                code_type=code_type)

    @staticmethod
    def change_lightness(rgb, light: int,
                         code_type: str = 'hex') -> str | RGB_type:
        '''Changes lightness on HSL value of color. Returns hex or rgb.'''
        Color.check_code(code_type)
        hsl = list(rgb_to_hls(*Color.rgb_to_rgb01(*rgb)))
        hsl[1] += light / 100
        dark_rgb = Color.rgb01_to_rgb(*hls_to_rgb(*hsl))
        dark_rgb = [int(x) for x in dark_rgb]
        
        if code_type == 'rgb':
            return dark_rgb

        if code_type == 'hex':
            return Color.rgb_to_hex(*dark_rgb)

    @staticmethod
    def hex_to_rgb(hexadecimal: str) -> RGB_type:
        '''Converts hexadecimal color code to RGB.'''
        r, g, b = [int(s, 16) for s in wrap(hexadecimal[1:], 2)]
        return (r, g, b)

    @staticmethod
    def rgb_to_hex(r: int, g: int, b: int) -> str:
        '''Converts RGB color code to hexadecimal.'''
        hexadecimal = "#" + "".join([f"{s:02x}"
                                     for s in (r, g, b)])
        return hexadecimal

    @staticmethod
    def rgb_to_rgb01(r: int, g: int, b: int) -> RGB_type:
        return (x / 255 for x in (r, g, b))

    @staticmethod
    def rgb01_to_rgb(r: int, g: int , b: int) -> RGB_type:
        return (x * 255 for x in (r, g, b))


colors = Colors(('miku', '#5dd4d8'), ('rin', '#ecd38c'),
                    ('darkrin', '#c6b176'), ('lgray', '#c0c0c0'))

fig, ax = plt.subplots()
