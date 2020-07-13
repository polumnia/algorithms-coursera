from dataclasses import dataclass
from typing import Optional
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from algorithms.priority_queue import MinPQ

@dataclass
class SearchNode:
    board: 'Board'
    moves: int = 0
    prev_node: Optional['SearchNode'] = None

    def __gt__(self, other):
        return self.board.manhattan() > other.board.manhattan()

class Board:

    def __init__(self, tiles):
        self.tiles = tiles
        self._dim = len(tiles)

    def __str__(self):
        row_str = [repr(row).strip("[]") for row in self.tiles]
        return f"{self._dim}\n" + "\n".join(row_str)

    def dimension(self) -> int:
        return self._dim

    def hamming(self):
        hamm_dist = 0
        for row_id in range(self._dim):
            for col_id in range(self._dim):
                if self.tiles[row_id][col_id] == 0:
                    continue
                goal_tile = self._get_goal_by_position(row_id, col_id)
                if self.tiles[row_id][col_id] != goal_tile:
                    hamm_dist += 1
        return hamm_dist


    def manhattan(self):
        dist = 0
        for row_id in range(self._dim):
            for col_id in range(self._dim):
                if self.tiles[row_id][col_id] == 0:
                    continue
                goal_row, goal_col = self._get_position_by_goal(self.tiles[row_id][col_id])
                dist += abs(goal_row - row_id) + abs(goal_col - col_id)
        return dist

    
    def _get_goal_by_position(self, row, col):
        return row * self._dim + col + 1
    
    def _get_position_by_goal(self, goal_tile):
        row_id = goal_tile // self._dim
        if goal_tile % self._dim == 0:
            row_id -= 1
            col_id = self._dim - 1
        else:
            col_id = goal_tile % self._dim - 1
        return row_id, col_id

    def is_goal(self):
        goal_board = [[self._get_goal_by_position(i, j) for j in range(self._dim)] for i in range(self._dim)]
        goal_board[self._dim - 1][self._dim - 1] = 0
        return self.tiles == goal_board

    def __eq__(self, other):
        self.tiles == other.tiles

    def neighbors(self):
        zero_row, zero_col = self._get_zero_pos()
        for row in (zero_row + 1, zero_row - 1):
            if (0 <= row <= self._dim - 1):
                new_tiles = [x[:] for x in self.tiles]
                new_tiles[zero_row][zero_col] = self.tiles[row][zero_col]
                new_tiles[row][zero_col] = self.tiles[zero_row][zero_col]
                yield new_tiles
        
        for col in (zero_col + 1, zero_col - 1):
            if (0 <= col <= self._dim - 1):
                new_tiles = [x[:] for x in self.tiles]
                new_tiles[zero_row][zero_col] = self.tiles[zero_row][col]
                new_tiles[zero_row][col] = self.tiles[zero_row][zero_col]
                yield new_tiles
        

    def twin(self):
        pass

    def _get_zero_pos(self):
        for row_id in range(self._dim):
             for col_id in range(self._dim):
                if self.tiles[row_id][col_id] == 0:
                    return row_id, col_id


class Solver:
    def __init__(self, init_board: Board):
        self.initial = init_board

    def is_solvable(self) -> bool:
        inversions = 0
        tiles = [item for row in self.initial for item in row]
        for i in range(len(tiles - 1)):
            for j in range(i + 1, len(tiles)):
                if tiles[i] and tiles[j] and tiles[i] > tiles[j]:
                    inversions += 1
        return inversions % 2 == 0

    def moves_to_solve(self) -> int:
        pass

    def solution(self):
        if not self.is_solvable():
            return None
        boards_pq = MinPQ()
        boards_pq.insert(SearchNode(self.initial))
        while True:
            min_board_node = boards_pq.del_min()
            min_board = min_board_node.board
            min_board_moves = min_board_node.moves
            if min_board.is_goal():
                break

            for neighbor in min_board.neighbors():
                if neighbor == min_board.prev_node.board.tiles:
                    continue
                boards_pq.insert(SearchNode(
                    Board(neighbor),
                    min_board_moves + 1,
                    min_board_node
                ))
        return min_board_node


if __name__ == '__main__':
    tiles = [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
    initial = Board(tiles)

    solver = Solver(initial)
    solution = solver.solution()
    print(f"Minimum number of moves = {solution.moves}")
    current_node = solution
    while current_node:
        print(current_node.board)
        current_node = current_node.prev_node
        print()