import csv

import os



def test_workers_are_adults():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(test_dir, '..', 'resources_hw8', 'people.csv')) as csv_file:
        users = csv.DictReader(csv_file, delimiter=';')
        print()
        workers = [user for user in users if user['status'] == 'worker']
        # for user in users:
        #     if user['status'] == 'worker':
        #         workers.append(user)

    for worker in workers:
        assert (
            int(worker['age']) >= 18
        ), f'The worker {worker["name"]} have {worker["age"]} year'
