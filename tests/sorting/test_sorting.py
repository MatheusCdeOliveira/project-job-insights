from src.pre_built.sorting import sort_by
from pytest import fixture


@fixture
def job_one():
    return {
        'job_title': 'Marketing',
        'company': 'Relief',
        'state': 'NY',
        'city': 'New York',
        'min_salary': '10899',
        'max_salary': '64093',
        'job_desc': 'Marketing operations of the company.',
        'industry': 'Finance',
        'rating': '4.0',
        'date_posted': '2020-05-08',
        'valid_until': '2020-06-07',
        'job_type': 'FULL_TIME',
        'id': '1'
    }


@fixture
def job_two():
    return {
        'job_title': 'Marketing',
        'company': 'Relief',
        'state': 'NY',
        'city': 'New York',
        'min_salary': '2899',
        'max_salary': '34093',
        'job_desc': 'Marketing operations of the company.',
        'industry': 'Finance',
        'rating': '5.0',
        'date_posted': '2020-09-28',
        'valid_until': '2020-06-07',
        'job_type': 'FULL_TIME',
        'id': '2'
    }


@fixture
def job_three():
    return {
        'job_title': 'Marketing',
        'company': 'Relief',
        'state': 'NY',
        'city': 'New York',
        'min_salary': '35599',
        'max_salary': '104053',
        'job_desc': 'Marketing operations of the company.',
        'industry': 'Finance',
        'rating': '7.0',
        'date_posted': '2021-02-21',
        'valid_until': '2020-06-07',
        'job_type': 'FULL_TIME',
        'id': '3'
    }


def test_sort_by_criteria(job_one, job_two, job_three):
    lst_jobs = [job_one, job_two, job_three]
    sort_by(lst_jobs, "date_posted")
    assert lst_jobs[0]["id"] == "3"

    sort_by(lst_jobs, "min_salary")
    assert lst_jobs[0]["id"] == "2"

    sort_by(lst_jobs, "max_salary")
    assert lst_jobs[0]["id"] == "3"
