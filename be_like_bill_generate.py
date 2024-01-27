from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_be_like_bill import Ui_Form


def create_image(name='Билл', text='Он знает сколько будет 2 + 2'):
    path = os.getcwd()

    os.chdir(sys._MEIPASS)
    SIZE = (500, 1000)
    new_image = Image.new("RGB", SIZE, (255, 255, 255))
    # рисуем человека
    # тело
    draw = ImageDraw.Draw(new_image)
    x1, y1 = SIZE[0] / 4 * 3, SIZE[1] / 5 * 2
    x2, y2 = x1, y1 + SIZE[1] / 5 * 1.2
    draw.line([x1, y1, x2, y2], fill=(0, 0, 0), width=5)
    # голова
    r = 40
    x1gol, y1gol = x1 - r, y1 - r
    x2gol, y2gol = x1gol + 2 * r, y1gol + 2 * r
    draw.ellipse([x1gol, y1gol, x2gol, y2gol], fill=(255, 255, 255), width=5, outline=(0, 0, 0))
    # лицо
    r = 10
    x1gol, y1gol = x1gol + 20, y1gol + 20
    x2gol, y2gol = x1gol + r, y1gol + r
    draw.ellipse([x1gol, y1gol, x2gol, y2gol], fill=(0, 0, 0))

    x1gol = x1gol + 20
    x2gol, y2gol = x1gol + r, y1gol + r
    draw.ellipse([x1gol, y1gol, x2gol, y2gol], fill=(0, 0, 0))

    x1gol -= 20
    x2gol += 10
    y2gol += 20
    draw.arc([x1gol, y1gol, x2gol, y2gol], start=0, end=180, fill=(0, 0, 0), width=5)

    # ноги
    x1_leg, y1_leg = x2, y2
    x2_leg, y2_leg = x2 + 40, y2 + 100
    x2_leg_2, y2_leg_2 = x2 - 40, y2 + 100
    draw.line([x1_leg, y1_leg, x2_leg, y2_leg], fill=(0, 0, 0), width=5)
    draw.line([x1_leg, y1_leg, x2_leg_2, y2_leg_2], fill=(0, 0, 0), width=5)
    # руки
    x1_arm, y1_arm = x1, y1 + 50
    x2_arm, y2_arm = x1_arm - 40, y1_arm + 50
    x2_arm_2, y2_arm_2 = x1_arm + 40, y1_arm + 50
    draw.line([x1_arm, y1_arm, x2_arm, y2_arm], fill=(0, 0, 0), width=5)
    draw.line([x1_arm, y1_arm, x2_arm_2, y2_arm_2], fill=(0, 0, 0), width=5)

    # текст
    text_ = f'Это {name}'
    font = ImageFont.truetype('default.ttf', size=32, encoding='UTF-8')
    draw.text((30, 350), text_, fill=(0, 0, 0), font_size=30, font=font)
    margin = 30
    offset = 400
    for line in textwrap.wrap(text, width=20):
        draw.text((margin, offset), line, font=font, fill=(0, 0, 0))
        offset += font.getbbox(line)[1] + 10
    text = f'{name} чёртов гений'
    offset += 50
    for line in textwrap.wrap(text, width=20):
        draw.text((margin, offset), line, font=font, fill=(0, 0, 0))
        offset += font.getbbox(line)[1] + 10
    draw.text((30, 600), f'будь как {name}', fill=(0, 0, 0), font_size=30, font=font)
    os.chdir(path)
    new_image.save('test.png', 'PNG')
    return path


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.generate.clicked.connect(self.on_click)

    def on_click(self):
        path = create_image(self.Name.text(), self.lineEdit_2.text())
        self.text.setText(path)


def gui():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
