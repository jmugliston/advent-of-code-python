# 🎄 Advent of Code (Python) 🎄

<div align="left">
    <img
      src="https://github.com/jmugliston/advent-of-code-python/raw/HEAD/aoc-python.jpeg"
      width="150"
      height="auto"
    />
</div>

Project for AOC challenges and solutions in Python.

## Setup

Create a .env file with the following:

```
SESSION_TOKEN=<aoc-session-token>
```

Install the package locally:

```sh
make install
```

## Test

Run tests with:

```sh
make test
# or
make test-watch
```

## CLI

```sh
aoc.py
```

### Usage

```
# aoc.py

🎄🎄🎄 Advent of Code 🎄🎄🎄

positional arguments:
  {init,solve,submit}  Sub-command help
    init               Initialise a new day
    solve              Solve a specific day
    submit             Submit the solution to a day

options:
  -h, --help           show this help message and exit
```

```
# aoc.py init --help

usage: aoc.py init [-h] --year {2015,2016,2017,2018,2019,2020,2021,2022,2023,2024}
                   --day
                   {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25}

options:
  -h, --help            show this help message and exit
  --year {2015,2016,2017,2018,2019,2020,2021,2022,2023,2024}
                        Year
  --day {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25}
                        Day
```

```
# aoc.py solve --help

usage: aoc.py solve [-h] --year {2015,2016,2017,2018,2019,2020,2021,2022,2023,2024} --day
                    {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25} [--part {1,2}]
                    [--example | --no-example]

options:
  -h, --help            show this help message and exit
  --year {2015,2016,2017,2018,2019,2020,2021,2022,2023,2024}
                        Year
  --day {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25}
                        Day
  --part {1,2}          Part
  --example, --no-example
                        Use example data
```

```
# aoc.py submit --help

usage: aoc.py submit [-h] --year {2015,2016,2017,2018,2019,2020,2021,2022,2023,2024} --day
                     {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25} [--part {1,2}]

options:
  -h, --help            show this help message and exit
  --year {2015,2016,2017,2018,2019,2020,2021,2022,2023,2024}
                        Year
  --day {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25}
                        Day
  --part {1,2}          Part
```