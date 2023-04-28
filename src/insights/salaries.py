from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_list = read(path)
    max_salary = []
    for x in jobs_list:
        if x["max_salary"].isdigit():
            max_salary.append(int(x["max_salary"]))
    return max(max_salary)


def get_min_salary(path: str) -> int:
    jobs_list = read(path)
    min_salary = []
    for x in jobs_list:
        if x["min_salary"].isdigit():
            min_salary.append(int(x["min_salary"]))
    return min(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min = job["min_salary"]
        max = job["max_salary"]
        if int(min) > int(max):
            raise ValueError
        return int(min) <= int(salary) <= int(max)
    except KeyError:
        raise ValueError
    except TypeError:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    lst_salary_filtered = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                lst_salary_filtered.append(job)
        except ValueError:
            print("invalid values")
    return lst_salary_filtered
