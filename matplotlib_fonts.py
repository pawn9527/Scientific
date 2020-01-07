# encoding: utf-8
"""
用来查找matplotlib 可以输入中文的字体.
"""
from matplotlib.font_manager import FontManager
import subprocess

fm = FontManager()
mat_fonts = set(f.name for f in fm.ttflist)
print(mat_fonts)
output = subprocess.check_output('fc-list :lang=zh -f "%{family}\n"', shell=True)
print('*' * 10, '系统可用的中文字体', '*' * 10)
# 这里 output 输出的bytes 需要转换为 str utf-8
print(output.decode("utf-8"))
zh_fonts = set(f.split(',', 1)[0] for f in output.decode("utf-8").split('\n'))
available = mat_fonts & zh_fonts
print('*' * 10, '可用的字体', '*' * 10)
for f in available:
    print(f)
