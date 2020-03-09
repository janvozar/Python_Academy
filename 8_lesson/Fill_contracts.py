# Task 56: Fill in contracts

TEMPLATE_PATH = '/home/janvozar/PycharmProjects/Python_Academy/8_lessonTemplates'
CONTRACTS_PATH = '/home/janvozar/PycharmProjects/Python_Academy/8_lesson/Contracts'
EMPLOYEE_DB_PATH = '/home/janvozar/PycharmProjects/Python_Academy/8_lesson/employees.txt'

TEMPLATES = ['salary change', 'job change', 'contract prolongation']

def main():
    num = int(input(print_prompt()))

    employees = load_db(EMPLOYEE_DB_PATH)

    template_name = TEMPLATES[num].replace(' ', '_')
    template = load_template(template_name)

    for employee_id, employee in employees.items():
        print('Creating contract for %s ....'%(employee_id,))
        write_file(employee, template, template_name)

    print('\nContracts have been generated.')

def print_prompt():
    print('Please select the option number of action you want to perform:\n')
    for temp in enumerate(TEMPLATES):
        print('{}. {}'.format(*temp))
    return '\n'


def load_db(path):
    employees_file = open(path)
    content = employees_file.read()
    employees_file.close()
    return eval(content)

def load_template(template_name):
    template_path = '{}/{}.txt'.format(TEMPLATE_PATH,template_name)

    with open(template_path) as template_file:
        template = template_file.read()

    return template

def write_file(employee,template, template_name):
    filename = '{}_{}.txt'.format(template_name,employee['full_name'])
    filepath = '{}/{}'.format(CONTRACTS_PATH, filename)

    with open(filepath,'w') as new_file:
        new_file.write(template.format(**employee))

main()