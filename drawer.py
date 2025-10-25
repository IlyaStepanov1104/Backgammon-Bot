from PIL import Image, ImageDraw, ImageFont

from const import *


# === Основная функция ===
def draw_checkers(state, dir, name):
    board = Image.open(BOARD_IMAGE_PATH).convert("RGBA")
    draw = ImageDraw.Draw(board)

    for player in ['first', 'second']:
        for point, count in state[player].items():
            if point == 'Bar':
                x, base_y = BAR_COORDS[player]
                direction = -1 if player == 'first' else 1
            else:
                real_point = point if player == 'first' else str(25 - int(point))
                x, base_y = POINT_COORDS[real_point]
                direction = 1 if int(real_point) > 12 else -1
                base_y += direction * CHECKER_RADIUS

            for i in range(count):
                y = base_y + i * direction * (CHECKER_RADIUS * 2 + 2)
                draw.ellipse(
                    (x - CHECKER_RADIUS, y - CHECKER_RADIUS, x + CHECKER_RADIUS, y + CHECKER_RADIUS),
                    fill=COLORS[player],
                    outline="gray"
                )
    board.save(f'{dir}/{name}.png')

