<h1>SOLVING TAPATAN WITH ADVERSARIAL SEARCH</h1>

## Introduction

This project is the fourth in a series of projects in which simple games will be developed using the pygame library, and these games will be conquered using machine learning algorithms and artificial intelligence in general.

The motivation behind this approach lies in frequent situations where certain evaluation metrics, when applied to specific algorithms, prove to be inaccurate and obscure their true practical significance. In extreme cases, algorithms with poor performance may be inaccurately assessed positively by specific metrics that, in practice, do not reflect their true effectiveness and distort their evaluation.

When developing algorithms to win games, we have two main evaluation metrics that are simple and have empirical significance:

1. Whether the algorithm won or not.
2. If it won, how efficient its performance was.

## Implementing the Tapatan

The tapatan game is implemented using the numpy library for game logic and the pygame library for the interface. It features three screens:

<p align="center">
    <img src="https://github.com/filipemedeiross/solving_tapatan_by_adversarial_search/blob/main/examples/home_screen.png" width="250" height="400">
</p>

This screen displays the initial board and a **Play** button to start the game with the current piece positions. Additionally, an **i** button links to the project developer's gitHub profile.

<p align="center">
    <img src="https://github.com/filipemedeiross/solving_tapatan_by_adversarial_search/blob/main/examples/game_screen.png" width="250" height="400">
</p>

Upon starting the game, it shows the time elapsed and the count of movements made, allowing users to return to the home screen, restart the game, or play their moves against an ai-controlled bot.

<p align="center">
    <img src="https://github.com/filipemedeiross/solving_tapatan_by_adversarial_search/blob/main/examples/winner_screen.png" width="250" height="400">
</p>

When a player wins (although losing or drawing against the bot is more common), time and movements halt, and interaction with the game is disabled. Options to return to the home screen or restart the game remain available.

## Search Strategies

This project presents a tapatan game bot powered by the minimax algorithm, renowned for its prowess in strategic gameplay, facilitating intelligent decision-making. Employing this technique, the bot meticulously evaluates all potential moves, strategically selecting the optimal choice while preempting the opponent's actions. To strike a balance between computational efficiency and strategic acumen, the minimax algorithm constructs a search tree with a maximum depth of 4, enabling the bot to forecast moves up to four steps ahead.

Extensive testing and experimentation have produced notable results, demonstrating the bot's adeptness in predicting opponent maneuvers and crafting effective strategic responses, as evidenced by its consistent victories against a random agent benchmark:

<p align="center">
    <img src="https://github.com/filipemedeiross/solving_tapatan/blob/main/examples/comparison_between_agents.png" width="500" height="400">
</p>

In assessing different search depths, a depth of 4 was selected for optimal performance. While there was improvement compared to a depth of 2, further increases to depths of 6 and 8 yielded negligible enhancements, compromising efficiency:

<p align="center">
    <img src="https://github.com/filipemedeiross/solving_tapatan/blob/main/examples/comparison_of_max_search_depth.png" width="500" height="400">
</p>

> Note: In assessing the efficacy of the minimax search compared to a random agent, and examining the impact of varying search depths, the following methodology is adopted:
> - Evaluation at search depths of 2, 4, 6, and 8
> - Analysis conducted over 20 games at each depth

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
            minimax.py           Solver using the minimax search
```

## Running the Game

Using some Linux distro and make sure you have [Python 3](https://www.python.org/) installed.

Clone the project:

```bash
  git clone https://github.com/filipemedeiross/solving_tapatan.git
```

Access the project directory:

```bash
  cd solving_tapatan
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
  python3 main.py
```

## References

Stuart Russell and Peter Norvig. **Artificial Intelligence: A Modern Approach**. 3rd ed., Pearson, 2009.

Numpy: <https://numpy.org/doc/stable/>

Pygame: <https://www.pygame.org/docs/>

Images and sounds used: <https://opengameart.org/>
