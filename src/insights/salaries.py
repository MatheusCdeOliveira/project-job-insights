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
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError

    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError

    if job["min_salary"] > job["max_salary"]:
        raise ValueError

    return job["min_salary"] <= int(salary) <= job["max_salary"]


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
