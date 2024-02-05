import csv


def test_workers_are_adults():
    with open('../resources_hw8/people.csv') as csv_file:
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
