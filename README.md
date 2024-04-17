<h1>SOLVING TAPATAN BY ADVERSARIAL SEARCH</h1>

## Implementing the Tapatan

The tapatan was implemented using the numpy library for the game logic and the pygame library for the interface. The game has three screens explained below:

![Home Screen](https://github.com/filipemedeiross/solving_tapatan_by_adversarial_search/blob/main/examples/home_screen.png)

The initial screen displays the game's initial board and the **Play** button that, when clicked, starts the game with the current state of the pieces. It also has an **i** button that takes you to the project developer's github profile.

![Game Screen](https://github.com/filipemedeiross/solving_tapatan_by_adversarial_search/blob/main/examples/game_screen.png)

When starting the game, it displays the time count and the movements performed, allowing the user to return to the initial screen, restart the game or perform the movements of the black pieces and play against a bot that uses AI.

![Winner Screen](https://github.com/filipemedeiross/solving_tapatan_by_adversarial_search/blob/main/examples/winner_screen.png)

When you win the game - most likely you will lose or play endlessly against the bot - time and movements are paused and interaction with the game is disabled. The functions of going back to the initial screen and restarting the game remain.

## Search Strategies

This project implements a bot for the tapatan game using the minimax algorithm, which is widely used in strategy games to make smart decisions. With this approach, the bot can evaluate all possible moves and choose the best option considering the opponent's moves.

The search tree created by the minimax algorithm has a maximum depth of 6 in order to obtain computational efficiency, this way the bot can only "think anticipating up to six moves". After testing and experimentation, we achieved remarkable results, with the bot showing the ability to predict the opponent's movements and find efficient strategic responses.

## Tapatan Pack Organization

```
tapatan/                         Top-level package
      __init__.py
      constants.py
      logic_game.py
      tapatan.py                 It brings together the functionalities of the modules to implement the tapatan
      media/                     Folder with the .png and .mp3 files used in the game's interface
              ...
      formulations/              Can be extended with different tapatan game formulations
            __init__.py
            standard_form.py     Sets the standard formulation of the problem
      solvers/                   Implementation of solvers
            __init__.py
            minimax/             Solver using the minimax search
                  __init__.py
                  minimax.py
```

## Running the Game

Using some Linux distro and make sure you have [Python 3](https://www.python.org/) installed.

Clone the project:

```bash
  git clone https://github.com/filipemedeiross/solving_tapatan_by_adversarial_search.git
```

Access the project directory:

```bash
  cd solving_tapatan_by_adversarial_search
```

Creating a virtual environment (for the example we use the location directory parameter as `.venv`):

```bash
  python3 -m venv .venv
```

Activating the virtual environment:

```bash
  source .venv/bin/activate
```

Install all required packages specified in requirements.txt:

```bash
  pip install -r requirements.txt
```

Use the following command to run the game:

```bash
  python3 -m tapatan.tapatan
```

## References

Russell, Stuart, J. e Peter Norvig. Inteligência Artificial: Uma Abordagem Moderna. Grupo GEN, 2022.

Images and sounds used: <https://opengameart.org/>

Numpy: <https://numpy.org/doc/stable/>

Pygame: <https://www.pygame.org/docs/>
