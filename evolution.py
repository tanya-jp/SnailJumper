import copy

from player import Player
import numpy as np
import random


class Evolution:
    def __init__(self):
        self.game_mode = "Neuroevolution"

    def next_population_selection(self, players, num_players):
        """
        Gets list of previous and current players (μ + λ) and returns num_players number of players based on their
        fitness value.

        :param players: list of players in the previous generation
        :param num_players: number of players that we return
        """
        # TODO (Implement top-k algorithm here)
        sorted_players = sorted(players, key=lambda player: player.fitness, reverse=True)
        # TODO (Additional: Implement roulette wheel here)
        # self.roulette_wheel(sorted_players, num_players)
        # TODO (Additional: Implement SUS here)
        self.sus(sorted_players, num_players)
        # TODO (Additional: Learning curve)
        return sorted_players[: num_players]

    def generate_new_population(self, num_players, prev_players=None):
        """
        Gets survivors and returns a list containing num_players number of children.

        :param num_players: Length of returning list
        :param prev_players: List of survivors
        :return: A list of children
        """
        first_generation = prev_players is None
        if first_generation:
            return [Player(self.game_mode) for _ in range(num_players)]
        else:
            # TODO ( Parent selection and child generation )
            # new_players = prev_players  # DELETE THIS AFTER YOUR IMPLEMENTATION
            new_players = self.crossover_players(prev_players)
            return new_players

    def crossover_players(self, prev_players):
        """
        Apply crossover on players inorder to make new children.
        :param prev_players: List of survivors
        :return: List of crossover children
        """
        new_players = []

        for i in range(0, len(prev_players), 2):
            prev_players1 = prev_players[i]
            prev_players2 = prev_players[i + 1]

            new_player1 = self.clone_player(prev_players1)
            new_player2 = self.clone_player(prev_players2)

            for i in range(len(new_player1.nn.w)):
                shape = new_player1.nn.w[i].shape
                # weight
                new_player1.nn.w[i][:, shape[1] // 2:] = prev_players2.nn.w[i][:, shape[1] // 2:]
                new_player2.nn.w[i][:, shape[1] // 2:] = prev_players1.nn.w[i][:, shape[1] // 2:]
                # bias
                new_player1.nn.b[i][:, shape[1] // 2:] = prev_players2.nn.b[i][:, shape[1] // 2:]
                new_player2.nn.b[i][:, shape[1] // 2:] = prev_players1.nn.b[i][:, shape[1] // 2:]

            new_players.append(new_player1)
            new_players.append(new_player2)

        return new_players

    def clone_player(self, player):
        """
        Gets a player as an input and produces a clone of that player.
        """
        new_player = Player(self.game_mode)
        new_player.nn = copy.deepcopy(player.nn)
        new_player.fitness = player.fitness
        return new_player

    def roulette_wheel(self, players, num_player):
        next_generation = []
        total_fits = sum([player.fitness for player in players])
        probabilities = [player.fitness / total_fits for player in players]
        for i in range(num_player):
            chosen = np.random.choice(players, 1, p=probabilities)
            next_generation.append(chosen)

        return next_generation

    def sus(self, players, num_players):
        next_generation = []
        total_fits = sum([player.fitness for player in players])
        probabilities = {}
        total_p = 0
        for i in range(len(players)):
            p = []
            p.append(total_p)
            total_p += players[i].fitness / total_fits
            p.append(total_p)
            probabilities[i] = p

        step = 1 / num_players
        start_point = random.uniform(0, step)
        pointers = [start_point + i * step for i in range(num_players)]
        player = 0
        for p in pointers:
            for i in range(len(players)):
                if probabilities[i][0] <= p < probabilities[i][1]:
                    next_generation.append(players[i])
                    break
        return  next_generation
