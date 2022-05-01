# Chum Sim Backend

## Description

[![GitHub Issues](https://img.shields.io/github/issues/MichaelJAliberti/chum_sim_backend.svg)](https://github.com/MichaelJAliberti/chum_sim_backend/issues)
[![License](https://img.shields.io/github/license/MichaelJAliberti/chum_sim_backend)](https://opensource.org/licenses/MIT)

Chum Sim is a Shadowrun management tool inspired by [Chummer 5](https://github.com/chummer5a/chummer5a).

Chum Sim allows users to create new characters, modify existing characters, and run simulations between characters in order to asses the quality of combat encounters. Chum Sim also allows users to make dice rolls digitally, streamlining gameplay at the table.

This repository contains the code for Chum Sim's backend api, which is intended to run on heroku. The frontend code may be found [here](https://github.com/MichaelJAliberti/chum_sim).

## Installation

Before starting, make sure you have [Git](https://git-scm.com/), [Python](https://www.python.org/), and [Pipenv](https://pypi.org/project/pipenv/) installed.

Then, run the followin commands in your terminal:

```
git clone https://github.com/MichaelJAliberti/chum_sim_backend.git
cd chum_sim_backend
pipenv install
```

## Running

Once installation is complete, start the program by running

```
pipenv shell
py main.py
```