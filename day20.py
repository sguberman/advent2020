import math
from collections import defaultdict
from typing import Dict, List, Tuple

from utils import elapsed_time, print_results

Tile = List[List[str]]
Tiles = Dict[int, Tile]
Edge = List[str]
Edges = Dict[str, Edge]
Variants = Dict[str, Tile]
Coordinate = Tuple[int, int]
Image = Dict[Coordinate, Tuple[int, Edges]]


def read_tiles(filename: str) -> Tiles:
    tiles = {}
    with open(filename) as f:
        for tile_str in f.read().split('\n\n'):
            tile_number, tile = read_tile(tile_str)
            tiles[tile_number] = tile
    return tiles


def read_tile(tile: str) -> Tuple[int, Tile]:
    header, *lines = tile.splitlines()
    tile_number = int(header.split()[1].strip(':'))
    rows = [list(line) for line in lines]
    return tile_number, rows


def flip_ud(tile: Tile) -> Tile:
    return tile[::-1]


def flip_lr(tile: Tile) -> Tile:
    return [row[::-1] for row in tile]


def rotate_cw(tile: Tile) -> Tile:
    return [[row[i] for row in reversed(tile)] for i in range(len(tile[0]))]


def tile_edges(tile: Tile) -> Edges:
    top = tile[0]
    bottom = tile[-1]
    left = [row[0] for row in tile]
    right = [row[-1] for row in tile]
    return {'top': top, 'bottom': bottom, 'left': left, 'right': right}


def all_variants(tile: Tile) -> Variants:
    variants: Variants = {}
    for rotation in range(2):
        variants[f'{rotation}-original'] = tile
        variants[f'{rotation}-ud'] = flip_ud(tile)
        variants[f'{rotation}-lr'] = flip_lr(tile)
        variants[f'{rotation}-ud-lr'] = flip_lr(flip_ud(tile))
        tile = rotate_cw(tile)
    return variants


def find_match(image: Image, tile: Tile) -> Tuple[Coordinate, str, Tile]:
    for variant in all_variants(tile).values():
        for side, edge in tile_edges(variant).items():
            for (x, y), (_id, edges) in image.items():
                if side == 'top':
                    try:
                        if edge == edges['bottom']:
                            edges.pop('bottom')
                            return (x, y + 1), side, variant
                    except KeyError:
                        pass
                elif side == 'bottom':
                    try:
                        if edge == edges['top']:
                            edges.pop('top')
                            return (x, y - 1), side, variant
                    except KeyError:
                        pass
                elif side == 'left':
                    try:
                        if edge == edges['right']:
                            edges.pop('right')
                            return (x + 1, y), side, variant
                    except KeyError:
                        pass
                else:  # side == 'right'
                    try:
                        if edge == edges['left']:
                            edges.pop('left')
                            return (x - 1, y), side, variant
                    except KeyError:
                        pass
    return None, None, None


def print_tile(tile: Tile) -> None:
    for row in tile:
        print(''.join(row))


def get_id(image: Image, coordinate: Coordinate) -> int:
    return image[coordinate][0]


def get_corner_ids(image: Image) -> List[int]:
    coordinates = image.keys()
    minx, maxx, miny, maxy = 0, 0, 0, 0
    for x, y in coordinates:
        if x < minx:
            minx = x
        if x > maxx:
            maxx = x
        if y < miny:
            miny = y
        if y > maxy:
            maxy = y
    corners = [(minx, miny), (minx, maxy), (maxx, miny), (maxx, maxy)]
    return [get_id(image, coordinate) for coordinate in corners]


def part1(filename: str) -> int:
    tiles = read_tiles(filename)
    tile_id, tile = tiles.popitem()
    image = {(0, 0): (tile_id, tile_edges(tile))}
    while tiles:
        tile_id, tile = tiles.popitem()  # LIFO
        coordinate, side, variant = find_match(image, tile)
        if coordinate:
            print(
                f"found match for {tile_id}, {len(tiles)} tiles remaining...")
            edges = tile_edges(variant)
            edges.pop(side)
            image[coordinate] = (tile_id, edges)
        else:
            tiles = {tile_id: tile} | tiles  # popitem is LIFO
    return math.prod(get_corner_ids(image))


def part2(filename: str) -> int:
    pass


if __name__ == '__main__':
    puzzle_input = 'input_day20.txt'
    print_results(elapsed_time(part1, puzzle_input),
                  elapsed_time(part2, puzzle_input))
