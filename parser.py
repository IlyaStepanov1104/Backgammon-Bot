import copy
import json
import re
from os import makedirs

from const import DEFAULT_PLACEMENT


def toggle_player(player):
    return 'second' if player == 'first' else 'first'


def parse_move_table(lines):
    result = []
    pattern = re.compile(r'^\s*(\d+)\)\s*(.*?)\s{2,}(.*?)\s*$')

    for line in lines:
        line = line.rstrip()

        match = pattern.match(line)
        if not match:
            continue

        move_number = int(match.group(1))
        player1_text = match.group(2).strip()
        player2_text = match.group(3).strip()

        # Извлечение кубиков
        def extract_dice(s):
            match = re.match(r'^(\d{2}):', s)
            return [int(s[0]), int(s[1])] if match else []

        dice1 = extract_dice(player1_text)
        dice2 = extract_dice(player2_text)

        result.append({
            'move': move_number,
            'player1': player1_text,
            'player2': player2_text,
            'dice1': dice1,
            'dice2': dice2
        })

    return result


def extract_names_and_scores(lines):
    pattern = re.compile(r'^(.*?)\s*:\s*(\d+)\s+(.*?)\s*:\s*(\d+)\s*$')
    for line in lines:
        match = pattern.match(line)
        if match:
            return {
                'first_name': match.group(1).strip(),
                'first_score': int(match.group(2)),
                'second_name': match.group(3).strip(),
                'second_score': int(match.group(4))
            }
    return {
        'first_name': 'Player 1',
        'first_score': 0,
        'second_name': 'Player 2',
        'second_score': 0
    }


def extract_point_match(text):
    pattern = re.compile(r'(\d+)\s+point match', re.IGNORECASE)
    match = pattern.search(text)
    if match:
        return int(match.group(1))
    return None


def extract_moves(player_moves):
    moves_list = []
    split_moves = player_moves.split(': ')
    if len(split_moves) == 1:
        return moves_list
    for move in split_moves[1].split():
        if '/' not in move:
            continue
        start, end = move.split('/')
        captured = False
        if end.endswith('*'):
            captured = True
            end = end[:-1]
        moves_list.append({
            'from': start,
            'to': end,
            'captured': captured
        })
    return moves_list


def parse_game(text, dir, points_match):
    makedirs(f'./json/{dir}', exist_ok=True)
    lines = text.strip().split('\n')
    header_data = extract_names_and_scores(lines)

    game_data = {
        "first": {
            "name": header_data['first_name'],
            "score": header_data['first_score']
        },
        "second": {
            "name": header_data['second_name'],
            "score": header_data['second_score']
        },
        "point_match": points_match,
        "turns": []
    }

    cube_owner = None
    cube_value = 1

    moves = parse_move_table(lines)

    for move in moves:
        for player_key in ['player1', 'player2']:
            player = 'first' if player_key == 'player1' else 'second'
            text_move = move[player_key]

            if not text_move:
                continue

            # Обработка куба Даве
            if 'Doubles =>' in text_move:
                cube_value = int(text_move.split('=>')[1].strip())
                cube_owner = toggle_player(player)
                game_data["turns"].append({
                    'turn': player,
                    'dice': [],
                    'cube_owner': cube_owner,
                    'cube_value': cube_value,
                    'moves': [],
                    'action': 'double'
                })
                continue

            if 'Takes' in text_move or 'Drops' in text_move:
                game_data["turns"].append({
                    'turn': player,
                    'dice': [],
                    'cube_owner': cube_owner,
                    'cube_value': cube_value,
                    'moves': [],
                    'action': 'take' if 'Takes' in text_move else 'drop'
                })
                continue

            # Обычные ходы
            dice = move['dice1'] if player_key == 'player1' else move['dice2']
            moves_list = extract_moves(text_move)

            game_data["turns"].append({
                'turn': player,
                'dice': dice,
                'cube_owner': cube_owner,
                'cube_value': cube_value,
                'moves': moves_list
            })

    with open(f'./json/{dir}/game.json', 'w+', encoding='utf-8') as file:
        json.dump(game_data, file, indent=2, ensure_ascii=False)
    return game_data


def parse_file(path, dir):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()

    split_file = re.split(r'\n\nGame \d\n', data)

    points_match = extract_point_match(split_file[0])

    games = split_file[1:]
    for i, game_text in enumerate(games):
        makedirs(f'./json/{dir}', exist_ok=True)
        parse_game(game_text, f'{dir}/{i + 1}', points_match)
    return [i for i in range(1, len(games) + 1)]
