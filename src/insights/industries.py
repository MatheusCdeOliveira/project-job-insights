from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_list = read(path)
    industry_types = set()
    for job in jobs_list:
        if job["industry"] != "":
            industry_types.add(job["industry"])
    return industry_types


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_by_industry = [x for x in jobs if x["industry"] == industry]
    return filtered_by_industry
