from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        job_reader = csv.DictReader(file)
        lst = list()
        for row in job_reader:
            lst.append(row)
        return lst


def get_unique_job_types(path: str) -> List[str]:
    job_list = read(path)
    job_types = set()
    for job in job_list:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    job_filtered = [item for item in jobs if item["job_type"] == job_type]
    return job_filtered
