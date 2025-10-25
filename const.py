BOT_TOKEN = '8165148569:AAE1TuZjz7dGhR8arVLxL4rJ9bUwhuecOMo'
YOUR_BOT_USERNAME = '@test_ajsncjsanjancsaj_bot'
WEB_APP_URL = 'https://nards-mini-app-ohft.vercel.app'
WEBHOOK_PATH='/api/bot'

DEFAULT_PLACEMENT = {
    'first': {
        'Bar': 0,
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 5,
        '7': 0,
        '8': 3,
        '9': 0,
        '10': 0,
        '11': 0,
        '12': 0,
        '13': 5,
        '14': 0,
        '15': 0,
        '16': 0,
        '17': 0,
        '18': 0,
        '19': 0,
        '20': 0,
        '21': 0,
        '22': 0,
        '23': 2,
        '24': 1,
    },
    'second': {
        'Bar': 0,
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 5,
        '7': 0,
        '8': 3,
        '9': 0,
        '10': 0,
        '11': 0,
        '12': 0,
        '13': 5,
        '14': 0,
        '15': 0,
        '16': 0,
        '17': 0,
        '18': 0,
        '19': 0,
        '20': 0,
        '21': 0,
        '22': 0,
        '23': 2,
        '24': 1,
    }
}


BOARD_IMAGE_PATH = 'board.jpg'  # путь к файлу доски
CHECKER_RADIUS = 30

COLORS = {
    'first': '#FFFFFF',  # белые
    'second': '#000000'  # черные
}

START_X_1 = 220
START_X_2 = 712
X_SPACE = 69

START_Y_1 = 985
START_Y_2 = 100

# Центры точек (для примера указаны фиктивные координаты, подставь свои реальные)
POINT_COORDS = {
    '1': (START_X_2 + X_SPACE * 5, START_Y_1),
    '2': (START_X_2 + X_SPACE * 4, START_Y_1),
    '3': (START_X_2 + X_SPACE * 3, START_Y_1),
    '4': (START_X_2 + X_SPACE * 2, START_Y_1),
    '5': (START_X_2 + X_SPACE * 1, START_Y_1),
    '6': (START_X_2 + X_SPACE * 0, START_Y_1),
    '7': (START_X_1 + X_SPACE * 5, START_Y_1),
    '8': (START_X_1 + X_SPACE * 4, START_Y_1),
    '9': (START_X_1 + X_SPACE * 3, START_Y_1),
    '10': (START_X_1 + X_SPACE * 2, START_Y_1),
    '11': (START_X_1 + X_SPACE * 1, START_Y_1),
    '12': (START_X_1 + X_SPACE * 0, START_Y_1),
    '13': (START_X_1 + X_SPACE * 0, START_Y_2),
    '14': (START_X_1 + X_SPACE * 1, START_Y_2),
    '15': (START_X_1 + X_SPACE * 2, START_Y_2),
    '16': (START_X_1 + X_SPACE * 3, START_Y_2),
    '17': (START_X_1 + X_SPACE * 4, START_Y_2),
    '18': (START_X_1 + X_SPACE * 5, START_Y_2),
    '19': (START_X_2 + X_SPACE * 0, START_Y_2),
    '20': (START_X_2 + X_SPACE * 1, START_Y_2),
    '21': (START_X_2 + X_SPACE * 2, START_Y_2),
    '22': (START_X_2 + X_SPACE * 3, START_Y_2),
    '23': (START_X_2 + X_SPACE * 4, START_Y_2),
    '24': (START_X_2 + X_SPACE * 5, START_Y_2),
}
# Пример центра для бара
BAR_COORDS = {
    'first': (640, 436),
    'second': (640, 496)
}

# Направление по оси Y: снизу вверх или сверху вниз
DIRECTION = {
    'first': 1,
    'second': -1
}