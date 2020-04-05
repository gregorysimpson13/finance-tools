from debt import Debt
import itertools
import copy


def read_csv(csv_file="real_data.csv"):
    with open(csv_file, 'r') as f:
        data = f.readlines()
    return data

def data_to_objects(data):
    debt_list = []
    for row in data:
        args = row.split(',')
        debt_list.append(Debt(*args))
    return debt_list

# the thing I dont like about this is that the minimum changes
# need to find a way to calculate the minimum payment for each
def distribute_payment(debt_list, monthly_contribution):
    for debt in debt_list:
        monthly_contribution -= debt.minimum_payment()
    return monthly_contribution

def distribute_extra(debt_list, monthly_contribution=0):
    for debt in debt_list:
        if monthly_contribution == 0:
            return
        if not debt.is_paid_off():
            monthly_contribution = debt.make_payment(monthly_contribution)
        

def calculate_montly_obligations(debt_list):
    total = 0
    for debt in debt_list:
        total += debt.get_minimum_payment()
    return total

def calculate_total_interest(debt_list):
    total_interest = 0
    for debt in debt_list:
        total_interest += debt.get_interest()
    return total_interest

def increment_monthly_interest(debt_list):
    for debt in debt_list:
        debt.roll_over_interest()

def debt_free(debt_list):
    for debt in debt_list:
        if not debt.is_paid_off():
            return False
    return True

def run_financial_analysis(debt_list, monthly_contribution):
    while not debt_free(debt_list):
        local_monthly_contribution = copy.deepcopy(monthly_contribution)
        increment_monthly_interest(debt_list)
        local_monthly_contribution = distribute_payment(debt_list, local_monthly_contribution)
        distribute_extra(debt_list, local_monthly_contribution)
    return calculate_total_interest(debt_list)

def main(debt_list, numbers_list):
    extra_payment = 362.17
    monthly_contribution = calculate_montly_obligations(debt_list) + extra_payment
    minimum_interest = float("inf")
    minimum_permutation = None
    for numbers_permutation in itertools.permutations(numbers_list):
        debt_permutation = []
        for number in numbers_permutation:
            debt_permutation.append(copy.deepcopy(debt_list[number]))
        total_interest = run_financial_analysis(debt_permutation, monthly_contribution)
        if total_interest < minimum_interest:
            minimum_interest = total_interest
            minimum_permutation = debt_permutation
    print(f'Minimum Interest = {minimum_interest:.2f}')
    for debt in minimum_permutation:
        print(debt.get_name())

if __name__ == "__main__":
    data = read_csv()
    debt_list = data_to_objects(data)
    numbers_list = [num for num in range(len(debt_list))]
    main(debt_list, numbers_list)

