import sys
import argparse
from datetime import datetime
import shutil
import os
import requests
from dotenv import load_dotenv
from markdownify import markdownify as md
from bs4 import BeautifulSoup
from loguru import logger

load_dotenv()

BASE_URL = "https://adventofcode.com"

SESSION_COOKIE = os.getenv("SESSION_TOKEN")
USER_AGENT = "github.com/jmugliston/advent-of-code-python 1.0.0"

logger.remove()
logger.configure(extra={"year": "", "day": "", "part": "1"})
logger.level("INFO", color="<light-green>")
logger.add(
    sys.stderr,
    format="{time:HH:mm:ss.SSS} <level>{level}</level> 🎄 <light-black>aoc:</> {message} <light-black>year=</>{extra[year]} <light-black>day=</>{extra[day]} <light-black>part=</>{extra[part]}",
)


def create_template(year, day):
    logger.info(f"Creating template", year=year, day=day, part=1)

    template_dir = "./template"
    destination_dir = f"./{year}/day{day:02d}"

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for item in os.listdir(template_dir):
        s = os.path.join(template_dir, item)
        d = os.path.join(destination_dir, item)
        if os.path.isdir(s):
            if not os.path.exists(d):
                shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            if not os.path.exists(d):
                shutil.copy2(s, d)


def download_question(year, day, part=1):
    logger.info(f"Downloading question", year=year, day=day, part=part)

    url = f"{BASE_URL}/{year}/day/{day}"

    headers = {"Cookie": f"session={SESSION_COOKIE}", "User-Agent": USER_AGENT}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article")
        question_text = "".join(str(article) for article in articles)
        markdown = md(question_text)
        question_dir = f"./{year}/day{day:02d}"
        with open(f"{question_dir}/README.md", "w") as f:
            f.write(markdown)
    else:
        logger.error(f"Failed to download question: {response.status_code}")


def download_input(year, day):
    logger.info(f"Downloading input", year=year, day=day, part=1)

    url = f"{BASE_URL}/{year}/day/{day}/input"
    headers = {"Cookie": f"session={SESSION_COOKIE}", "User-Agent": USER_AGENT}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        input_dir = f"./{year}/day{day:02d}/input"
        os.makedirs(input_dir, exist_ok=True)
        with open(f"{input_dir}/input.txt", "w") as f:
            f.write(response.text)
    else:
        logger.error(f"Failed to download input: {response.status_code}")


def get_solution(year, day, part, example=False):
    logger.info(f"Solving", year=year, day=day, part=part)

    script_path = f"./{year}/day{day:02d}/main.py"
    if os.path.exists(script_path):
        command = f"python {script_path} --part {part}"
        result = os.popen(command).read()
        return result.strip()
    else:
        logger.error(f"Script {script_path} does not exist.")


def submit_solution(year, day, part, answer):
    logger.info(f"Submitting solution", year=year, day=day, part=part)

    url = f"{BASE_URL}/{year}/day/{day}/answer"
    headers = {"Cookie": f"session={SESSION_COOKIE}", "User-Agent": USER_AGENT}

    data = {
        "level": part,
        "answer": answer,
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        article = soup.find("article")
        print(article.text)
        return True
    else:
        print(response.text)
        return False


def init(year, day):
    create_template(year, day)
    download_question(year, day)
    download_input(year, day)


def solve(year, day, part):
    answer = get_solution(year, day, part)
    print(answer)


def submit(year, day, part):
    answer = get_solution(year, day, part)
    solved = submit_solution(year, day, part, answer)
    if part == 1 and solved:
        download_question(year, day, part=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🎄🎄🎄 Advent of Code 🎄🎄🎄")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    current_year = datetime.now().year

    def add_common_arguments(subparser, include_part=True):
        subparser.add_argument(
            "--year",
            type=int,
            required=True,
            help="Year",
            choices=range(2015, current_year),
        )
        subparser.add_argument(
            "--day",
            type=int,
            required=True,
            help="Day",
            choices=range(1, 26),
        )
        if include_part:
            subparser.add_argument(
                "--part", type=int, choices=[1, 2], default=1, help="Part"
            )

    parser_init = subparsers.add_parser("init", help="Initialise a new day")
    add_common_arguments(parser_init, False)

    parser_solve = subparsers.add_parser("solve", help="Solve a specific day")
    add_common_arguments(parser_solve)

    parser_submit = subparsers.add_parser("submit", help="Submit the solution to a day")
    add_common_arguments(parser_submit)

    args = parser.parse_args()

    if args.command == "init":
        init(args.year, args.day)
    elif args.command == "solve":
        solve(args.year, args.day, args.part)
    elif args.command == "submit":
        submit(args.year, args.day, args.part)
    else:
        parser.print_help()
