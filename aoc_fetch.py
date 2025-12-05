import datetime
import os
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


def fetch_test_case(year, day, session_cookie, dir_path):
    """
    Fetches the Advent of Code test case for a given year and day from the puzzle page.

    Args:
        year (int): The year of the puzzle.
        day (int): The day of the puzzle.
        session_cookie (str): The Advent of Code session cookie.
        dir_path (str): The directory path to save the test case.
    """
    puzzle_url = f'https://adventofcode.com/{year}/day/{day}'
    cookies = {'session': session_cookie}

    try:
        response = requests.get(puzzle_url, cookies=cookies)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Error fetching puzzle page from {puzzle_url}: {e}')
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <pre><code> blocks which typically contain example inputs
    code_blocks = soup.find_all('pre')

    if not code_blocks:
        print(
            f'No test case code blocks found on {puzzle_url}. Skipping test.txt creation.'
        )
        return

    # Take the content of the first <pre> block as the test case
    test_case_content = code_blocks[0].get_text().strip()

    test_file_path = os.path.join(dir_path, 'test.txt')
    try:
        with open(test_file_path, 'w') as f:
            f.write(test_case_content)
        print(f'Successfully saved test case to {test_file_path}')
    except IOError as e:
        print(f'Error writing test case to file {test_file_path}: {e}')


def fetch_aoc_input(year, day):
    """
    Fetches the Advent of Code input for a given year and day.

    Args:
        year (int): The year of the puzzle.
        day (int): The day of the puzzle.
    """
    load_dotenv()
    session_cookie = os.getenv('AOC_SESSION')
    if not session_cookie:
        print('Error: AOC_SESSION cookie not found in .env file.')
        sys.exit(1)

    day_str = f'{day:02d}'
    dir_path = os.path.join(str(year), f'day{day_str}')

    if os.path.exists(dir_path):
        print(f'Directory {dir_path} already exists. Aborting.')
        return

    try:
        os.makedirs(dir_path)
        print(f'Created directory: {dir_path}')
    except OSError as e:
        print(f'Error creating directory {dir_path}: {e}')
        sys.exit(1)

    url = f'https://adventofcode.com/{year}/day/{day}/input'
    cookies = {'session': session_cookie}

    try:
        response = requests.get(url, cookies=cookies)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        print(f'Error fetching input from {url}: {e}')
        sys.exit(1)

    input_file_path = os.path.join(dir_path, 'input.txt')
    try:
        with open(input_file_path, 'w') as f:
            f.write(response.text)
        print(f'Successfully saved input to {input_file_path}')
    except IOError as e:
        print(f'Error writing to file {input_file_path}: {e}')
        sys.exit(1)

    # Fetch and save the test case after fetching the main input
    fetch_test_case(year, day, session_cookie, dir_path)

    # script
    script_path = os.path.join(dir_path, f'day{day:02d}.py')
    template = """import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from utils import utils

INPUT = utils.read_input_lines('input.txt')
"""
    with open(Path(script_path), 'w') as f:
        f.write(template)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        year = datetime.datetime.today().year
        day = datetime.datetime.today().day
    elif len(sys.argv) == 2:
        year = datetime.datetime.today().year
        try:
            day = int(sys.argv[1])
        except ValueError:
            print('Error: Day must be integer.')
            sys.exit(1)
    elif len(sys.argv) == 3:
        try:
            year = int(sys.argv[1])
            day = int(sys.argv[2])
        except ValueError:
            print('Error: Year and day must be integers.')
            sys.exit(1)
    else:
        print(
            """Usage:
- python aoc_fetch.py <year> <day>
- python aoc_fetch.py <day> (default to current year)
- python aoc_fetch.py (default to current day and year)
            """
        )
        sys.exit(1)

    fetch_aoc_input(year, day)
