# UEFA Euro 2024

Simple pronostics for Euro 2024 football cup based on Bradley-Terry and some past data.

## HOWTO
- Fill out `input_data/uefa-data-euro24.csv` with most up to date results;
- In `conf.py`, fill out `ALL_GAMES`  with the games you want a pronostic for, and `TITLE` with the title you want for the graph that will be generated;
- Run `01_make_games_list.py` then `02_bradley_terry.py` then `03_pronostics_from_bt.py`
- See in the terminal for easy to read pronostics, and see in `boxplots/` for a nice graph.

## Round 3

![Pool3](boxplots/_03_whisk-2023-03-01-2024-07-31.png)

## Round 2

![Pool2](boxplots/_02_whisk-2023-03-01-2024-07-31.png)

## Round 1

![Pool1](boxplots/_01_whisk-2023-03-01-2024-03-31.png)